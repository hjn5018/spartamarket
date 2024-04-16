from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.


def index(request):
    return render(request, 'products/index.html')


def products(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)


def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('products:product_detail', product.id)
    else:
        form = ProductForm()
    context ={'form':form}
    return render(request, 'products/create.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {
        'product':product
    }
    return render(request, 'products/product_detail.html', context)


def delete(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:products')
    return redirect('products:product_detail', product.pk)


def update(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect('products:product_detail', product.id)
    else:
        forms = ProductForm(instance=product)
    context = {
        'forms':forms,
        'product':product,
    }
    return render(request, 'products/update.html', context)
