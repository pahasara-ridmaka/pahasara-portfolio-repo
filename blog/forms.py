from django import forms
from .models import Post


class WriteForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["author","title", "body","thumbnail"]
