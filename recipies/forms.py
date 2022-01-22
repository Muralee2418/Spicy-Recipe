from django import forms
from .models import comments
from .models import ScrapRecipie

class commentforms(forms.ModelForm):
    class Meta:
        model=comments
        fields=['comment_info']

class recipieforms(forms.ModelForm):
    class Meta:
        model=ScrapRecipie
        exclude=['author']