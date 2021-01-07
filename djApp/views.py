from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from djApp.models import Category,Product

# Create your views here.

def category_list(request):
    #return HttpResponse("Esta es mi primera url")
    data={
        'title':'Listado de Categorias',
        'categories':Category.objects.all()
    }
    return render(request,"category/category_list.html",data)

""" def products(request):
    data={
        'products':Product.objects.all()
    }
    return render(request,'product_page.html',data)

def static_files(request):
    return render(request,'static_files.html') """