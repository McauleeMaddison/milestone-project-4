import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': 500,
                'product_data': {'name': 'Iced Coffee'},
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/payments/success/',
        cancel_url='http://127.0.0.1:8000/payments/cancel/',
    )
    return redirect(session.url, code=303)

def payment_success(request):
    return HttpResponse("✅ Payment successful. Thank you!")

def payment_cancel(request):
    return HttpResponse("❌ Payment cancelled.")
