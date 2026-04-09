from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Q, Avg

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'query': query
    })

from cart.forms import CartAddProductForm
from .forms import ReviewForm
from .models import Review
from django.shortcuts import redirect

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    reviews = product.reviews.all()
    # Calcular promedio de estrellas
    avg_data = reviews.aggregate(avg=Avg('rating'))
    avg_rating = round(avg_data['avg'] or 0, 1)
    avg_rating_int = round(avg_data['avg'] or 0)  # Para renderizar estrellas llenas
    if request.method == 'POST' and request.user.is_authenticated:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            Review.objects.create(
                product=product,
                user=request.user,
                rating=review_form.cleaned_data['rating'],
                comment=review_form.cleaned_data['comment']
            )
            return redirect(product.get_absolute_url())
    else:
        review_form = ReviewForm()
    return render(request, 'shop/product/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'reviews': reviews,
        'review_form': review_form,
        'avg_rating': avg_rating,
        'avg_rating_int': avg_rating_int,
    })

def contact(request):
    return render(request, 'shop/contact.html')
