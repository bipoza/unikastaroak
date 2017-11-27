from django import forms
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import categories

class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Izenburua'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Edukia'}))
    url = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'http://www.uni.hezkuntza.net/web/guest/inicio', 'type':'url'}),required=False)
    drive_url = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'https://drive.google.com/drive/my-drive', 'pattern':'https?://drive.google.com/.+', 'title':'Sartu google drive-eko partekatze esteka', 'type':'url'}),required=False)
    category = forms.CharField(widget=forms.Select(choices=categories, attrs={'class':'form-control'}),required=True)
    class Meta:
        model = Article
        fields = ('title', 'text','category', 'url', 'drive_url' )

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        
class UserFormEdit(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'value':'********'}))
    class Meta:
        model = User
        fields = ('username','password','first_name', 'last_name', 'email')