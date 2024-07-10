from django.shortcuts import render
from bangazonapi.models import Order

def orders_report(request):
    status = request.GET.get('status', None)

    if status is not None and status == 'incomplete':
        orders = Order.objects.filter(payment_type__isnull=True).select_related('customer', 'customer__user')
        context = {'orders': orders}
        return render(request, 'incomplete_orders.html', context)
