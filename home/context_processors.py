from django.utils import timezone

def cart_details(request):
    cart = request.session.get('cart', [])
    
    # Check if session has expired
    last_activity_time_str = request.session.get('_session_last_activity')
    last_activity_time = timezone.datetime.fromisoformat(last_activity_time_str) if last_activity_time_str else None
    
    if last_activity_time is not None and timezone.now() > last_activity_time + timezone.timedelta(hours=1):
        request.session['cart'] = []
        cart = []
    
    total_amount = 0
    for item in cart:
        try:
            total_amount += float(item['amount'])
        except ValueError:
            pass
    
    # Update last activity time as a string
    request.session['_session_last_activity'] = str(timezone.now())
    
    return {
        'cart': cart,
        'total_amount': total_amount,
        'cart_count': len(cart)
    }
