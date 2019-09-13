from eobot import get_config, get_balances


def set_config(user_id, email, password):
    """ configure eobot module """
    get_config().configure(user_id=user_id, email=email, password=password)


def get_balance(currency):
    """ return the balance of a specific currency"""
    balances = get_balances()
    return balances[currency]
    # error requests.exceptions.ReadTimeout