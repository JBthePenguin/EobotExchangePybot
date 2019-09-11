from eobot_api.coins import get_coins
from eobot_api.user import get_ghs_balance
from eobot_api.exchange import get_amount
from config.config import USER_ID

# Coins
coins = get_coins()
print(coins)

# GHS5 balance
ghs_balance = get_ghs_balance(USER_ID)
print(ghs_balance)

# Estimate amount after exchange
amount = get_amount("GHS5", "BTC", ghs_balance)
print(amount)
