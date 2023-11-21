from django import forms
from .models import Comment



class CommentForm(forms.ModelForm):
    """
    This is a comments form
    """
    class Meta:
        model = Comment
        fields = ('body',)

