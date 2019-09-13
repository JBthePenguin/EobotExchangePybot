from eobot_api.coins import get_coins
from eobot_api.user import set_config
from config.real_config import USER_ID, EMAIL, PASSWORD
from eobot_api.mining import change_mining_mode, get_mode, get_monthly_revenue
from eobot_api.exchange import get_amount, exchange
from eobot_api.user import get_balance
import httpx
import json
import datetime
from time import sleep

# Configure user
set_config(USER_ID, EMAIL, PASSWORD)

# estimate ghs gain
# old_monthly_revenue = get_monthly_revenue()
# old_hourly_revenue = old_monthly_revenue['Cloud2SHA-256'] / 732
# old_estimate_ghs = get_amount("USD", "GHS5", old_hourly_revenue)
# mining speed
# mining_speed = get_mining_speed()
# print(mining_speed)

# coins supported
coins_supported = get_coins()
coins_supported.remove("CURE")
coins_supported.remove("STEEM")
coins_supported.remove("TRX")
coins_supported.remove('XEM')


# test
RUN = True
while RUN:
    # coins profit
    r = httpx.get("https://whattomine.com/calculators.json")
    coins = json.loads(r.text)
    coins_dict = coins["coins"]
    coins_stats = {}
    for key, value in coins_dict.items():
        if value["tag"] in coins_supported:
            coins_stats[key] = value
    coins_profit = {}
    for key, value in coins_stats.items():
        r = httpx.get(
            "https://whattomine.com/coins/" + str(value["id"]) + ".json")
        stat = json.loads(r.text)
        coins_profit[value["tag"]] = float(stat['profit'].replace("$", ""))
    # mine the more profitable coin
    more_profitable_coin = max(coins_profit, key=coins_profit.get)
    change_mining_mode(more_profitable_coin)
    now = datetime.datetime.now()
    print(coins_profit)
    print(
        now.strftime("%H:%M:%S"),
        " More profitable coin: ", more_profitable_coin,
        " - Mining mode: ", get_mode())
    sleep(600)
    amount = get_balance(more_profitable_coin) / 2
    exchange(more_profitable_coin, amount)
    now = datetime.datetime.now()
    print(
        now.strftime("%H:%M:%S"),
        " Exchange ", amount, " ", more_profitable_coin)

# estimate ghs gain
# new_monthly_revenue = get_monthly_revenue()
# new_hourly_revenue = new_monthly_revenue['Cloud2SHA-256'] / 732
# new_estimate_ghs = get_amount("USD", "GHS5", new_hourly_revenue)
# change_mining_mode("GHS5")
# estimate_ghs_with_coin = 0.95 * get_amount(
#     more_profitable_coin, "GHS5", get_balance(more_profitable_coin))

# print(
#     "Before: hourly revenue -> $", old_hourly_revenue,
#     "  estimate_ghs -> ", old_estimate_ghs, " GHS5")
# print(
#     "After: hourly revenue -> $", new_hourly_revenue,
#     "  estimate_ghs -> ", new_estimate_ghs, " GHS5")
# print(
#     "Estimate with ", more_profitable_coin, " -> ",
#     estimate_ghs_with_coin, " GHS5")
