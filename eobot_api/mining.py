from eobot import (
    get_mining_estimates, get_mining_speed,
    set_mining_mode, get_mining_mode)


def get_monthly_revenue():
    return get_mining_estimates()


def get_speed_mining():
    return get_mining_speed()


def change_mining_mode(currency):
    set_mining_mode(currency)


def get_mode():
    return get_mining_mode()
