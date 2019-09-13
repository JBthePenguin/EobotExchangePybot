from eobot import get_exchange_estimate, exchange_coins
from .user import get_balance


def get_amount(sell, buy, amount):
    """ return the estimate amount of buy currency
    for the amount of sell currency """
    return get_exchange_estimate(sell, buy, amount)


def exchanges(quantity, coin_one, coin_two):
    """ exchanges """
    exchange_coins("BTC", quantity, coin_one)
    exchange_coins(coin_one, get_balance(coin_one), coin_two)
    exchange_coins(coin_two, get_balance(coin_two), "BTC")


def exchange(coin, quantity):
    exchange_coins(coin, quantity, "GHS5")
