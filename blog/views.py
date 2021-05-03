from django.shortcuts import render
from blog.models import post


# Create your views here.
def blog(request):
    posts=post.objects.all()
    return render(request,"blog/blog.html",{"posts":posts})

def categoria(request,categoria_id):
    categoria= Categoria.objects.get(id=categoria_id)
    post=posts.objects.filter(categorias=categoria)
    return render(request,"blog/categoria.html", {"categoria":categoria,"posts":posts})
