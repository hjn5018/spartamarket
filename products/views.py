from django.shortcuts import render, redirect
from .models import Product
# Create your views here.


def index(request):
    return render(request, 'index.html')


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    product = Product(title=title, content=content)
    product.save()
    return redirect('product_detail', product.id)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product':product
    }
    return render(request, 'product_detail.html', context)


def delete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return redirect('product_detail', product.pk)


def edit(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product':product
    }
    return render(request, 'edit.html', context)


def update(request, pk):
    product = Product.objects.get(id=pk)
    product.title = request.POST.get('title')
    product.content = request.POST.get('content')
    product.save()
    return redirect('product_detail', product.id)