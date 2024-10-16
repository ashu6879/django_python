from django import forms
from .models import MyItem  # Updated import

class ItemCreateForm(forms.ModelForm):  # Keep the form class name
    class Meta:
        model = MyItem  # Updated model reference
        fields = ['name', 'description']
