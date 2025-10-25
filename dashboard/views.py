from django.shortcuts import render, get_object_or_404
from products.models import Product

# Homepage with product grid
def home(request):
    products = Product.objects.all()
    return render(request, 'dashboard/home.html', {'products': products})

# Customize a product: ingredient and size selection
def customize_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    ingredients = [
        "Ice", "Milk", "Soy Milk", "Oat Milk", "Whipped Cream",
        "Caramel Drizzle", "Chocolate Syrup", "Espresso Shot", "Sugar-Free"
    ]

    sizes = ["Small", "Medium", "Large"]

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
        "sizes": sizes,
    })

# Dashboard page (placeholder)
def user_dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# Settings page (placeholder)
def settings_view(request):
    return render(request, 'dashboard/settings.html')
