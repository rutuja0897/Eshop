from django.shortcuts import render,HttpResponse
from .models.product import Product

# Create your views here.

def index(request):
    prds=Product.get_all_products();
    print(prds)
    return render(request,'index.html',{'products':prds})
