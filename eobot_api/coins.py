from eobot import get_supported_coins


def get_coins():
    """ return a list of supported coins"""
    coins = get_supported_coins()
    coins = [*coins]
    return coins
