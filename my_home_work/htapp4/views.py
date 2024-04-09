from django.shortcuts import render, redirect
from django.urls import reverse

from htapp2.models import Product
from htapp4.forms import ProductForm


def get_product_by_id(request, success_message=None):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        return redirect(reverse('product_update', args=(product_id,)))
    return render(request, 'htapp4/update_product.html', {'success_message': success_message})


def product_update(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            success_message = f"Product with ID {product_id} successfully updated."
            return redirect('get_product_by_id', success_message=success_message)
    else:
        form = ProductForm(instance=product)
    return render(request, 'htapp4/product.html', {'form': form})


def product_create(request):
    success_message = None
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            new_product = Product(name=name, description=description, price=price, quantity=quantity)
            new_product.save()
            success_message = f"Product successfully created with ID {new_product.pk}."

    form = ProductForm()
    return render(request, 'htapp4/product_create.html',
                  {'form': form, 'success_message': success_message})

# Create your views here.
