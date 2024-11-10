from django import forms
from .models import profile

class add_form(forms.ModelForm):
    class Meta:
        model=profile
        fields=[
            'first_name',
            'last_name',
            'email',
            'image',
        ]