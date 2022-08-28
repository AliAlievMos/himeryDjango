from urllib import request

from django.shortcuts import render

from .models import Number, Block, Material
from authors.models import Authors

def index(requests):
    mag = Number.objects.order_by('-published')
    blocks = Block.objects.order_by('-spell')
    mat = Material.objects.order_by('-spell')
    context = {'mag': mag, 'blocks': blocks, 'mat': mat}
    
    return render(requests, 'mag/index.html', context)

def index_for_last(requests):
    
    maglast = Number.objects.earliest('-published')
    blocks = Block.objects.filter(number=maglast.id).order_by('-spell').reverse()
    mat = Material.objects.filter(number=maglast.id).order_by('-spell').reverse()


    context = {'maglast': maglast, 'blocks': blocks, 'mat': mat}
    
    return render(requests, 'maglast/index.html', context)


def index_for_click(requests, mag_id):
    maglast = Number.objects.get(id=mag_id)
    blocks = Block.objects.filter(number=maglast.id).order_by('-spell').reverse()
    mat = Material.objects.filter(number=maglast.id).order_by('-spell').reverse()
    context = {'maglast': maglast, 'blocks': blocks, 'mat': mat}

    return render(requests, 'maglast/index.html', context)

def material_page(requests, material_id):

    mat = Material.objects.filter(id=material_id).earliest('-name')
    author = Authors.objects.filter(id=mat.auth_id)
    context = {'mat': mat, 'author' : author }
    return render(requests, 'mat/index.html', context)

def search_result(requests):
    no_result = ''
    query = requests.GET.get('q')
    s = str(query).title().split(' ')
    mag = Number.objects.filter(name=s[0])
    blocks = Block.objects.filter(name=s[0])
    mat = Material.objects.filter(name=s[0])
    author = Authors.objects.filter(name=s[0])
    if not author:
        author = Authors.objects.filter(soname=s[0])
    for i in s:
        if not mag:
            mag = Number.objects.filter(name=i)
        if not blocks:
            blocks = Block.objects.filter(name=i)
        if not mat:
            mat = Material.objects.filter(name=i)
        if not author:
            author = Authors.objects.filter(name=i)
        if not author:
            author = Authors.objects.filter(soname=i)
    mat_textt = Material.objects.all()
    def f(mat_textt):
        for m in mat_textt:
            for i1 in s:
                if i1 in m.text.title():
                    mat_text = Material.objects.filter(id=m.id)
                    return mat_text
    mat_text = f(mat_textt)
    if not mag and not blocks and not mat and not author and not mat_text:
        no_result = 'ничего не найдено'
    context = {'mag': mag, 'blocks': blocks, 'mat': mat,'author' : author, 'query': query, 's': s,
               'mat_text': mat_text, 'no_result': no_result}

    return render(requests, 'search/index.html', context)

def search(requests):
    return render(requests, 'search/index.html')


