from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            continue 

        product = get_object_or_404(Product, pk=item_id)
        quantity = item_data['quantity']
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'a_measurement': item_data.get('a_measurement'),
            'b_measurement': item_data.get('b_measurement'),
            'bridge_measurement': item_data.get('bridge_measurement'),
            'temple_length': item_data.get('temple_length'),
            'lens_colour': item_data.get('lens_colour')
            
        })

    if total < settings.FREE_SHIPPING_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_SHIPPING_PERCENTAGE / 100)
        free_shipping_delta = settings.FREE_SHIPPING_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_shipping_delta = Decimal('0.00')

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_shipping_delta': free_shipping_delta,
        'free_shipping_threshold': settings.FREE_SHIPPING_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
