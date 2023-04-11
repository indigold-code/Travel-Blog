from django import forms
from .models import Post 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'summary', 'adventure_date')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'adventure_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': '2015-08-23'}, ),
    
        }
