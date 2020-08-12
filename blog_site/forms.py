from django import forms
from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={"class": "name_article", "placeholder": "Введите название статьи"}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "text_article"
        }
    ))
    image = forms.FileField(required=False, widget=forms.TextInput(
        attrs={"id": "fileupload", "type": "file", "name": "files[]", "style": 'display: none;'}
    ))
