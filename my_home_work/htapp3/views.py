from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from htapp2.models import Client, Order, Product


def main(request):
    return render(request, "htapp3/main.html")


def about(request):
    return render(request, "htapp3/about.html")


def get_orders_by_client(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        if client_id:
            return HttpResponseRedirect(reverse('all_client_orders', args=[client_id]))
    return render(request, 'htapp3/get_orders_by_client.html')


def all_client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client)
    products = Product.objects.filter(order__customer=client)
    return render(request, 'htapp3/all_client_orders.html', {'client': client, 'orders': orders, 'products': products})

# Create your views here.
