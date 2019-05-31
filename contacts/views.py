from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from .contacts_utils import *

def index(request):
    return render(request, 'contacts/contact_index.html')

class Mycontact_list(ListView):
    model = MyContacts
    context_object_name = 'people'

class Mycontact_create(CreateView):
    template_name = 'contacts/mycontacts_form2.html'
    model = MyContacts
    form_class = MyContactForm
    success_url = reverse_lazy('mycontact-list')

class Mycontact_update(UpdateView):
    model = MyContacts
    form_class = MyContactForm
    #success_url = reverse('mycontact-detail', args=(self.pk,))

    def get_success_url(self):
        url = reverse('mycontact-detail', args=(self.object.id,))
        return url

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['extra'] = get_extra_info(self, self.object.id)
        context['mycontact']=self.object
        return context

def mycontact_detail(request,pk):

    context={
        'mycontact':MyContacts.objects.get(id=pk),
        'extra': get_extra_info(request, pk)
    }
    return render(request, 'contacts/mycontact_detail2.html', context)

class Mycontact_delete(DeleteView):
    model = MyContacts
    success_url = reverse_lazy('mycontact-list')

def myphone_list(request,pk):
    telefon = ContactPhone.objects.filter(empunya=pk)
    contact = MyContacts.objects.get(id=pk)
    context = { 'phone':telefon, 'contact':contact }
    return render(request, 'contacts/myphone_list.html', context)

def myphone_create(request, pk):

    if request.method == 'POST':
        #name = 'testing'
        form = ContactPhoneForm(pk, request.POST)
        if form.is_valid():
            form.save()
            reurl = '/contacts/mycontact/update/' + str(pk)
            return HttpResponseRedirect(reurl)
    else:
        form = ContactPhoneForm(pk)
    return render(request, 'contacts/contactphone_form.html', {
        'form': form,
        'pk':pk,
    })

def myphone_update(request, pk, pid):
    phone = ContactPhone.objects.get(id=pid)
    if request.method == 'POST':
        form = ContactPhoneForm(pk, request.POST, instance=phone)
        if form.is_valid():
            form.save()
            reurl = '/contacts/mycontact/update/' + str(pk)
            return HttpResponseRedirect(reurl)
    else:
        form = ContactPhoneForm(pk, instance=phone)
    return render(request, 'contacts/contactphone_form.html', {
        'form': form,
        'pk': pk,
    })

def myphone_delete(request,pk, pid):
    myphone = ContactPhone.objects.get(id=pid)
    try:
        myphone.delete()
    except:
        pass
    return HttpResponseRedirect(reverse('mycontact-update', args=[pk,]))

def myemail_list(request, pk):
    telefon = ContactEmail.objects.filter(empunya=pk)
    contact = MyContacts.objects.get(id=pk)
    context = {'phone': telefon, 'contact': contact}
    return render(request, 'contacts/myemail_list.html', context)

def myemail_create(request,pk):
    if request.method == 'POST':
        form = ContactEmailForm(pk, request.POST)
        if form.is_valid():
            form.save()
            reurl = '/contacts/mycontact/update/' + str(pk)
            return HttpResponseRedirect(reurl)
    else:
        form = ContactEmailForm(pk)
    return render(request, 'contacts/contactemail_form.html', {
        'form': form,
        'pk': pk,
    })

def myemail_update(request, pk, pid):
    email = ContactEmail.objects.get(id=pid)
    if request.method == 'POST':
        form = ContactEmailForm(pk, request.POST, instance=email)
        if form.is_valid():
            form.save()
            reurl = '/contacts/mycontact/update/' + str(pk)
            return HttpResponseRedirect(reurl)
    else:
        form = ContactEmailForm(pk, instance=email)
    return render(request, 'contacts/contactemail_form.html', {
        'form': form,
        'pk': pk,
    })

def myemail_delete(request, pk, pid):
    myemail = ContactEmail.objects.get(id=pid)
    try:
        myemail.delete()
    except:
        pass
    return HttpResponseRedirect(reverse('mycontact-update', args=[pk, ]))


def myaddress_list(request, pk):
    telefon = ContactAddress.objects.filter(empunya=pk)
    contact = MyContacts.objects.get(id=pk)
    context = {'phone': telefon, 'contact': contact}
    return render(request, 'contacts/myaddress_list.html', context)

def myaddress_create(request, pk):
    if request.method == 'POST':
        form = ContactAddressForm(pk, request.POST)
        if form.is_valid():
            form.save()
            reurl = '/contacts/mycontact/update/' + str(pk)
            return HttpResponseRedirect(reurl)
    else:
        form = ContactAddressForm(pk)
    return render(request, 'contacts/contactaddress_form.html', {
        'form': form,
        'pk': pk,
    })


def myaddress_update(request, pk, pid):
    alamat=ContactAddress.objects.get(id=pid)
    if request.method == 'POST':
        form = ContactAddressForm(pk, request.POST, instance=alamat)
        if form.is_valid():
            form.save()
            reurl = '/contacts/mycontact/update/' + str(pk)
            return HttpResponseRedirect(reurl)
    else:
        form = ContactAddressForm(pk, instance=alamat)
    return render(request, 'contacts/contactaddress_form.html', {
        'form': form,
        'pk': pk,
    })

def myaddress_delete(request, pk, pid):
    myaddress = ContactAddress.objects.get(id=pid)
    try:
        myaddress.delete()
    except:
        pass
    return HttpResponseRedirect(reverse('mycontact-update', args=[pk, ]))
