from eobot import get_exchange_estimate


def get_amount(sell, buy, amount):
    """ return the estimate amount of buy currency
    for the amount of sell currency """
    return get_exchange_estimate(sell, buy, amount)
