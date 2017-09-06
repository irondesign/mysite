from django import forms
from Blog.models import Posts


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'text',
        )