from django import forms

from .models import Post

# Model form for a new post
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        labels = {
            'content': ''
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'maxlength': 1000, 'class': 'form-control', 'placeholder': 'What are you thinking?'})
        }