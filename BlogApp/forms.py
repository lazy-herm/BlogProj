from django import forms
from BlogApp.models import  Post, Comments

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')7

        widgets = {
            'title':forms.TextInput(attr={'class':'textinputclass'}),
            'text':forms.Textarea(attr={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attr={'class':'textinputclass'}),
            'text':forms.Textarea(attr={'class':'editable medium-editor-textarea'})
        }