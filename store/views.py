from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import Category


# Create your views here.
def store(request,category_slug=None):
    category=None
    products=None
    if category_slug!=None:
        category=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=category,is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    product_count=products.count
    context={
        'products':products,
        'product_count':product_count
    }
    return render(request,'store/store.html',context)

def product_details(request,category_slug,product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        context = {
        'single_product': single_product,
        }
    except Exception as e:
        raise e
    return render(request,'store/product_detail.html',context)