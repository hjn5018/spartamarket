from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products.html', context)


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', product.id)
    else:
        form = ProductForm()
    context ={'form':form}
    return render(request, 'create.html', context)


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