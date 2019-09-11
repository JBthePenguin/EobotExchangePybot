from eobot import get_config, get_balances


def get_ghs_balance(user_id):
    """ return the GHS5 balance """
    get_config().configure(user_id=user_id)
    balances = get_balances()
    return balances['GHS5']
