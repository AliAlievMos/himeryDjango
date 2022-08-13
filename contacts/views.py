from django.shortcuts import render

from .models import Contacts

def index(requests):
    contacts = Contacts.objects.all()
    return render(requests, 'contacts/index.html', {'contacts': contacts})