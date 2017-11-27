from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article
from .forms import ArticleForm, UserFormEdit, CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import categories

# Create your views here.
def article_list(request):
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'tutorials/article_list.html', {'articles':articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'tutorials/article_detail.html', {'article': article})

@login_required
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            #print(form.url_drive)
            article = form.save(commit=False)
            article.author = request.user
           # article.published_date = timezone.now()
            article.save()
            return redirect ('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'tutorials/article_edit.html', {'form':form})
    
@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    current_user = request.user
    if current_user.id == article.author_id: 
        if request.method == "POST":
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                return redirect('article_detail', pk=article.pk)
        else:
            form = ArticleForm(instance=article)
        
        return render(request, 'tutorials/article_edit.html', {'form': form})
    else:
        return redirect('/')
        
    
    
@login_required
def article_draft_list(request):
    if request.user.is_authenticated():
        userid = request.user.id
    articles = Article.objects.filter(published_date__isnull=True, author_id=userid).order_by('created_date')
    return render(request, 'tutorials/articles_draft_list.html', {'articles': articles})
    
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.published_date = timezone.now()
    article.save()
    return redirect('article_detail', pk=pk)   
    
def article_remove(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = CreateUserForm()
    return render(request, 'registration/register.html', {'form': form})
    
def profile(request, username):
    user = User.objects.get(username=username)
    userArticles = Article.objects.filter(author_id=user.id).filter(published_date__isnull=False).order_by('-published_date')
    userArticlesDrafts = Article.objects.filter(author_id=user.id).filter(published_date__isnull=True)
    #form = UserFormEdit(initial={'username': user.username, 'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email})
    return render(request, 'registration/profile.html', {'user': user, 'userArticles':userArticles, 'userArticlesDrafts':userArticlesDrafts})

def user_articles(request, username):
    user = User.objects.get(username=username)
    articles= Article.objects.filter(author_id=user.id).exclude(published_date__isnull=True)
    return render(request, 'tutorials/article_list.html',{'articles':articles})
    
def categories_list(request):
    categories= Article.objects.exclude(category__isnull=True).values_list('category', flat=True).distinct()
    return render(request, 'tutorials/categories_list.html',{'categories':categories})

def article_list_category(request, categoryParam):
    print(categoryParam)
    articles = Article.objects.filter(published_date__lte=timezone.now(), category=categoryParam).order_by('-published_date')
    return render(request, 'tutorials/article_list.html', {'articles':articles})
