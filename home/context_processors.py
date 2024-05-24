from django.utils import timezone

def cart_details(request):
    cart = request.session.get('cart', [])
    
    # Check if session has expired
    last_activity_time = request.session.get('_session_last_activity')
    if last_activity_time is not None and timezone.now() > last_activity_time + timezone.timedelta(hours=1):
        request.session['cart'] = []
        cart = []
    
    total_amount = 0
    for item in cart:
        try:
            total_amount += float(item['amount'])
        except ValueError:
            pass
    
    # Update last activity time
    request.session['_session_last_activity'] = timezone.now()
    
    return {
        'cart': cart,
        'total_amount': total_amount,
        'cart_count': len(cart)
    }