from django.shortcuts import render
from .models import Product
# Create your views here.


def index_html(request):

    products = Product.objects.all()

    return render(request, "index.html", {
        "produtcs": products
    })


