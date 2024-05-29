from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
import json



def view_bag(request):
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    a_measurement = float(request.POST.get('a_measurement'))
    b_measurement = float(request.POST.get('b_measurement'))
    bridge_measurement = float(request.POST.get('bridge_measurement'))
    temple_length = float(request.POST.get('temple_length'))
    lens_options = request.POST.get('lens_option')

    

    bag = request.session.get('bag', {})

    if item_id in bag:
        if isinstance(bag[item_id], dict):
            bag[item_id]['quantity'] += quantity
        else:
            bag[item_id] = {
                'quantity': quantity,
                'a_measurement': a_measurement,
                'b_measurement': b_measurement,
                'bridge_measurement': bridge_measurement,
                'temple_length': temple_length,
                'lens_option': lens_options
            }
    else:
        bag[item_id] = {
            'quantity': quantity,
            'a_measurement': a_measurement,
            'b_measurement': b_measurement,
            'bridge_measurement': bridge_measurement,
            'temple_length': temple_length,
            'lens_option': lens_options,
        }
        
    request.session['bag'] = json.loads(json.dumps(bag))

    return redirect(redirect_url)
