from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

def index(request):
    return render(request, 'products/index.html')


def products(request):
    products = Product.objects.all().order_by('-id')
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('products:product_detail', product.id)
    else:
        form = ProductForm()
    context ={'form':form}
    return render(request, 'products/create.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    comment_form = CommentForm()
    comments = product.comments.all()
    context = {
        'product':product,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'products/product_detail.html', context)

@require_POST
def delete(request, pk):
    if request.ust.in_authenticated:
        product = get_object_or_404(Product, id=pk)
        product.delete()
    return redirect('products:products')

@login_required
@require_http_methods(['GET', 'POST'])
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

@require_POST
def create_comment(request, pk):
    product = get_object_or_404(Product, id=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.save()
    return redirect('products:product_detail', pk)