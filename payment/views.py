import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        # Marcar la orden como pagada (En producción se usa confirmación via Webhook)
        order.paid = True
        order.save()
        return redirect('payment:completed')
    else:
        # El monto debe estar en centavos para Stripe
        amount = int(order.get_total_cost() * 100)
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                payment_method_types=['card'],
                metadata={'order_id': order.id}
            )
            client_secret = intent.client_secret
        except stripe.error.StripeError as e:
            # En caso de no tener API key válida, enviar vacío
            client_secret = ""

        return render(request, 'payment/process.html', {
            'order': order,
            'client_secret': client_secret,
            'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
        })

def payment_completed(request):
    return render(request, 'payment/completed.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')
