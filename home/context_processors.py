def cart_details(request):
    cart = request.session.get('cart', [])
    total_amount = 0
    for item in cart:
        try:
            total_amount += float(item['amount'])
        except ValueError:
            pass
    return {
        'cart': cart,
        'total_amount': total_amount,
        'cart_count': len(cart)
    }