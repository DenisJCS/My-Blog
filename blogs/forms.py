from django import forms
from .models import Post, Blogs

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        labels = {'text': 'Text field'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
        
