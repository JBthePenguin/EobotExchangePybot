from eobot_api.coins import get_coins
from eobot_api.user import get_ghs_balance
from config.config import USER_ID

# Coins
coins = get_coins()
print(coins)

# GHS5 balance
ghs_balance = get_ghs_balance(USER_ID)
print(ghs_balance)
