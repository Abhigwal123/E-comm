from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import Product

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'shop/product_list.html', {'page_obj': page_obj})

def signup(request):
    if request.method == 'POST':
        # Add signup logic here
        pass
    return render(request, 'shop/signup.html')

def login_user(request):
    if request.method == 'POST':
        # Add login logic here
        pass
    return render(request, 'shop/login.html')
