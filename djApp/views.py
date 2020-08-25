from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from djApp.models import Category,Product

# Create your views here.

def myfirstview(request):
    #return HttpResponse("Esta es mi primera url")
    data={
        'name':'Carlitox',
        'categories':Category.objects.all()
    }
    return render(request,"index.html",data)

def products(request):
    data={
        'products':Product.objects.all()
    }
    return render(request,'product_page.html',data)

def static_files(request):
    return render(request,'static_files.html')