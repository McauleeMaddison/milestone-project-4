from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from .models import CoffeeTrend, Subscription
import stripe
import json
from django.views.decorators.csrf import csrf_exempt

# Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


# ✅ Homepage view — shows static coffee shop page
def home(request):
    return render(request, "dashboard/home.html")


# ✅ Paid/free data access view
@login_required
def trends(request):
    # Check if the user has an active subscription
    is_paid = Subscription.objects.filter(user=request.user, active=True).exists()

    if is_paid:
        data = CoffeeTrend.objects.all()
    else:
        data = CoffeeTrend.objects.filter(is_premium=False)

    return render(request, "dashboard/trends.html", {"data": data, "paid": is_paid})


# ✅ Stripe checkout session creation
@login_required
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": "Premium Coffee Insights Subscription",
                },
                "unit_amount": 500,  # $5.00
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="http://localhost:8000/success/",
        cancel_url="http://localhost:8000/cancel/",
        customer_email=request.user.email,
    )

    return redirect(session.url, code=303)


# ✅ Stripe webhook to activate user subscriptions
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    # Handle checkout completion
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        email = session.get("customer_email")
        from django.contrib.auth.models import User
        try:
            user = User.objects.get(email=email)
            Subscription.objects.update_or_create(user=user, defaults={"active": True})
        except User.DoesNotExist:
            pass

    return HttpResponse(status=200)


# ✅ Payment success page
def success(request):
    return render(request, "dashboard/success.html")


# ✅ Payment cancel page
def cancel(request):
    return render(request, "dashboard/cancel.html")