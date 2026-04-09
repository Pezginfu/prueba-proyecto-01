from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # Clear the cart
            cart.clear()
            
            # Send confirmation email
            subject = f'Pedido nr. {order.id} - My Shop'
            message = f'Estimado {order.first_name},\n\nTu pedido ({order.id}) fue generado. Aguardando confirmación de pago.'
            send_mail(subject, message, 'admin@myshop.com', [order.email])
            
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order/history.html', {'orders': orders})
