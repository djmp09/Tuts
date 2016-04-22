from django import forms
from .models import log_in

class User(forms.ModelForm):

    class Meta:
        model = log_in
        fields = ('username', 'password',)