from .models import *

def get_extra_info(self,pk):
    alamat=ContactAddress.objects.filter(empunya=pk)
    email=ContactEmail.objects.filter(empunya=pk)
    phone=ContactPhone.objects.filter(empunya=pk)
    retdata={
        'alamat':alamat,
        'email':email,
        'phone':phone,
    }
    return retdata