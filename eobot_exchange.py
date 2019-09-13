from eobot_api.coins import get_coins
from eobot_api.user import set_config, get_balance
from eobot_api.exchange import get_amount, exchanges
from config.real_config import USER_ID, EMAIL, PASSWORD

# Coins
coins = get_coins()
print(coins)

# Configure user
set_config(USER_ID, EMAIL, PASSWORD)
# BTC balance
btc_balance = 1
# btc_balance = get_balance("BTC")
print(btc_balance)

stop = False

coins.remove("CURE")
coins.remove("BTC")
coins.remove("STEEM")
coins.remove("TRX")
coins.remove('XEM')

coins_without_coin_one = get_coins()
coins_without_coin_one.remove("CURE")
coins_without_coin_one.remove("BTC")
coins_without_coin_one.remove("STEEM")
coins_without_coin_one.remove("TRX")
coins_without_coin_one.remove('XEM')

# Estimate amount after exchange
for coin_one in coins:
    coins_without_coin_one.remove(coin_one)
    for coin_two in coins_without_coin_one:
        amount_coin_one = 0.95 * get_amount("BTC", coin_one, btc_balance)
        amount_coin_two = 0.95 * get_amount(
            coin_one, coin_two, amount_coin_one)
        new_btc_balance = 0.95 * get_amount(coin_two, "BTC", amount_coin_two)
        if new_btc_balance > btc_balance:
            # exchanges(btc_balance, coin_one, coin_two)
            # print(
            #     "BTC -> ", coin_one, " -> ", coin_two,
            #     " -> BTC !!! YES BENEFIT: ", get_balance("BTC") - btc_balance,
            #     " BTC")
            print(
                btc_balance, " BTC -> ", amount_coin_one, " ", coin_one,
                " -> ", amount_coin_two, " ", coin_two,
                " -> ", new_btc_balance, "BTC !!! YES BENEFIT: ",
                new_btc_balance - btc_balance, " BTC")
            stop = True
            break
        else:
            # print(
            #     "BTC -> ", coin_one, " -> ", coin_two,
            #     " -> BTC !!! NO BENEFIT")
            print(
                btc_balance, " BTC -> ", amount_coin_one, " ", coin_one,
                " -> ", amount_coin_two, " ", coin_two,
                " -> ", new_btc_balance, "BTC !!! NO BENEFIT: ",
                new_btc_balance - btc_balance, " BTC")
    if stop:
        break
    coins_without_coin_one.append(coin_one)

# 184.97687346
