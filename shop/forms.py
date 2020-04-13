from django import forms
from .models import PhotoSet


class PhotoSetForm(forms.ModelForm):
    class Meta:
        model = PhotoSet
        fields = ('title', 'description', 'preview_image', 'photo_set', 'tag', 'published_date')
