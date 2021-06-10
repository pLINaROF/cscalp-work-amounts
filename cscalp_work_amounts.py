import requests
import xml.etree.ElementTree as ET
import os

WorkAmountsUsdt = input('Введите 5 рабочих объемов в USDT через пробел и нажмите Enter\nПример: 100 200 300 400 33\n')
WorkAmountsUsdt = list(map(int, WorkAmountsUsdt.split(' ')))

if len(WorkAmountsUsdt) != 5:
    exit('Объемов должно быть 5')

exchangeInfo = requests.request("GET", "https://www.binance.com//fapi/v1/exchangeInfo").json()
prices = requests.request("GET", "https://www.binance.com/fapi/v1/ticker/price").json()
# print(prices)
futures_prices = {}
for price in prices:
    futures_prices[price["symbol"]] = price["price"]


def work_amount(WorkAmountsUsdt, price, stepSize):
    price = float(price)
    stepSize = float(stepSize)
    WorkAmountsLots = []
    for wa in WorkAmountsUsdt:
        result = wa / price // stepSize * stepSize
        # print(wa)
        # print(result)
        if stepSize < 1:
            WorkAmountsLots.append(round(float(result), len(symbol["filters"][1]["stepSize"].split('.')[1])))
        elif stepSize == 1 or result % 1 == 0:
            WorkAmountsLots.append(int(result))
    # print(WorkAmountsLots)
    return WorkAmountsLots


futures_all_work_amounts_lots = {}

print('symbol, price, stepSize, WorkAmountsUsdt')
for symbol in exchangeInfo["symbols"]:
    try:
        wa = work_amount(WorkAmountsUsdt, futures_prices[symbol["symbol"]], symbol["filters"][2]["stepSize"])
        futures_all_work_amounts_lots[symbol["symbol"]] = wa
        print(symbol["symbol"], futures_prices[symbol["symbol"]], symbol["filters"][2]["stepSize"], wa)
    except:
        pass
        # print(symbol["symbol"], 'не удалось рассчитать')

# # тест
# for f in futures_all_work_amounts_lots.items():
#     print(f)
# exit()


# Запись в Cscalp
def update_work_amounts_in_cscalp_tmp(file, wa):
    tmp = ET.ElementTree(file=file)
    for user_levels in tmp.iter('First_WorkAmount'):
        user_levels.set('Value', f'{wa[0]}')
    for user_levels in tmp.iter('Second_WorkAmount'):
        user_levels.set('Value', f'{wa[1]}')
    for user_levels in tmp.iter('Third_WorkAmount'):
        user_levels.set('Value', f'{wa[2]}')
    for user_levels in tmp.iter('Fourth_WorkAmount'):
        user_levels.set('Value', f'{wa[3]}')
    for user_levels in tmp.iter('Fifth_WorkAmount'):
        user_levels.set('Value', f'{wa[4]}')
    tmp.write(file, "UTF-8")


input('\nРабочие объемы рассчитаны\nУбедитесь что Cscalp не запущен и нажмите Enter')

exchange_name = 'BINANCE'
for file in os.listdir():
    # print(file)
    try:
        exchange, spot_or_fut, setting_name, n = file.split('.')
        symbol, settings, key = setting_name.split('_')
        # print(file, cscalp_levels_format(all_levels[symbol_name]))
        if spot_or_fut == 'CCUR_FUT' and exchange_name[0:4] in exchange:
            wa = futures_all_work_amounts_lots[symbol]
            update_work_amounts_in_cscalp_tmp(file, wa)
    except:
        pass

print('Запись завершена. Можно запускать Cscalp')
