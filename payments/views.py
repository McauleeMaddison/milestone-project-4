import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_coffee(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': 500,
                'product_data': {
                    'name': 'Iced Coffee',
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/payments/success/',
        cancel_url='http://127.0.0.1:8000/payments/cancel/',
    )

    return render(request, 'payments/checkout.html', {
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })

def payment_success(request):
    return render(request, 'payments/success.html')

def payment_cancel(request):
    return render(request, 'payments/cancel.html')
