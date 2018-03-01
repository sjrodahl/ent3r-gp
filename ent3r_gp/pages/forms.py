from django import forms
from .models import Activity

class NewActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('name', 'points')


