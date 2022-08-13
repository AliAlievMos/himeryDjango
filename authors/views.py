from django.shortcuts import render

from .models import Authors
from mag.models import Material

def index(requests):
    authors = Authors.objects.order_by('-soname').reverse()
    return render(requests, 'authors/index.html', {'authors': authors})

def index_auth(requests, author_id):
    author = Authors.objects.get(id=author_id)
    mat = Material.objects.filter(auth_id=author.id)
    context = {'author': author, 'mat': mat}
    return render(requests, 'authors/author/index.html', context)
