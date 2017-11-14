from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Izenburua'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Edukia'}))
    class Meta:
        model = Article
        fields = ('title', 'text',)