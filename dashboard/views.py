from django.shortcuts import render, get_object_or_404
from products.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'dashboard/home.html', {'products': products})

def customize_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    ingredients = [
        "Ice", "Milk", "Soy Milk", "Oat Milk", "Whipped Cream",
        "Caramel Drizzle", "Chocolate Syrup", "Espresso Shot", "Sugar-Free"
    ]

    if request.method == "POST":
        selected_ingredients = request.POST.getlist("ingredients")
        size = request.POST.get("size")

        return render(request, "dashboard/confirm.html", {
            "product": product,
            "ingredients": selected_ingredients,
            "size": size,
        })

    return render(request, "dashboard/customize.html", {
        "product": product,
        "ingredients": ingredients,
    })
