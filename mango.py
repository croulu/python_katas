UNITARY_PRICE = 3


def mango(quantity, price):
    return pay_how_much(quantity) * price


def offer_how_much(quantity):
    offer = quantity // 3
    return offer


def pay_how_much(quantity):
    return quantity - offer_how_much(quantity)


# mango(3, 12)
# offer_how_much(0)
