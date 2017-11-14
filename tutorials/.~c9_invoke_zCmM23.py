from django.shortcuts import render
#from django.utils import simplejson

# Create your views here.
def article_list(request):
    return render(request, 'blog/post_list.html', {})