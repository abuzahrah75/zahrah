from django import forms
from .models import *


class MyContactForm(forms.ModelForm):
    class Meta:
        model = MyContacts
        fields = ('nama', 'ringkas', 'no_kp_baru', 'no_kp_lama', 'no_passport', 'warganegara')


class ContactPhoneForm(forms.ModelForm):
    class Meta:
        model = ContactPhone
        fields = ('nombor', 'kategori','keutamaan','remark','empunya')
    
    def __init__(self,mypk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['empunya'].queryset = MyContacts.objects.filter(id=mypk)


class ContactEmailForm(forms.ModelForm):
    class Meta:
        model = ContactEmail
        fields = ('email', 'kategori', 'keutamaan', 'remark', 'empunya')

    def __init__(self, mypk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['empunya'].queryset = MyContacts.objects.filter(id=mypk)


class ContactAddressForm(forms.ModelForm):
    class Meta:
        model = ContactAddress
        fields = '__all__'

    def __init__(self, mypk, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['empunya'].queryset = MyContacts.objects.filter(id=mypk)
