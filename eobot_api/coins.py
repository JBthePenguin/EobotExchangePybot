from eobot import get_supported_coins


def get_coins():
    """ return a list of supported coins"""
    response = False
    while not response:
        try:
            coins = get_supported_coins()
        except RuntimeError:
            print("error")
        else:
            coins = [*coins]
            response = True
    return coins
