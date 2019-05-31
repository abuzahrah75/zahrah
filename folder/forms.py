from django import forms
from .models import *


class ClientFolderForm(forms.ModelForm):
    class Meta:
        model = ClientFolder
        fields = '__all__'
