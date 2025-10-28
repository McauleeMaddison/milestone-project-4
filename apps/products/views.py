from django.shortcuts import render
from django.http import Http404

PRODUCTS = [
    {"slug": "glacier-brew", "name": "Glacier Brew", "img": "img/products/glacier-brew.jpg"},
    {"slug": "polar-mocha", "name": "Polar Mocha", "img": "img/products/polar-mocha.jpg"},
    {"slug": "aurora-latte", "name": "Aurora Latte", "img": "img/products/aurora-latte.jpg"},
]

def index(request):
    return render(request, "products/index.html", {"products": PRODUCTS})

def detail(request, slug):
    for p in PRODUCTS:
        if p["slug"] == slug:
            return render(request, "products/detail.html", {"product": p})
    raise Http404("Product not found")
