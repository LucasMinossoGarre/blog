from django.shortcuts import render
from .models import Art

def home(request):
    artigos = Art.objects.all().order_by('-id')
    return render(request,'blog/pages/home.html',context={
        'artigo':artigos,
    })
