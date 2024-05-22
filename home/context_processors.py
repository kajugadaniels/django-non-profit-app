def cart_details(request):
    cart = request.session.get('cart', [])
    total_amount = sum(float(item['amount']) for item in cart)
    return {
        'cart': cart,
        'total_amount': total_amount,
        'cart_count': len(cart)
    }