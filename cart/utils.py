def calculate_cart_total(cart, movies_in_cart):
    """
    Calculate the total price for all items in the cart.

    Args:
        cart (dict): Session cart data with movie IDs as keys and quantities as values
        movies_in_cart (QuerySet): Movie objects that are in the cart

    Returns:
        float: Total price for all items in cart
    """
    total = 0
    for movie in movies_in_cart:
        quantity = cart.get(str(movie.id), 0)
        total += movie.price * int(quantity)
    return total