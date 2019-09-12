# import json
# import requests
#
# gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
# symbol = 'btcusd'
#
# btc_data = requests.get(gemini_ticker.format(symbol)).json()
# print(json.dumps(btc_data,indent=4))
# print(type(json.dumps(btc_data,indent=4)))
# dic = eval(json.dumps(btc_data,indent=4))  # src--->dic的转换
# print(type(dic)) #查看对象的类型
# print(dic['ask'])


## 绘制比特币未来一小时的走势


import matplotlib.pylab as plt
import pandas as pd
import requests

#获取数据的时间段
periods = '3600'

# 通过Http抓取btc的历史的价格走势
resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
                    params={
                        'periods':periods
                    },verify=False)
data = resp.json()

print(type(data))
# print(data['result'][periods])
df = pd.DataFrame(
    data['result'][periods],
    columns=[
        'CloseTime',
        'OpenPrice',
        'HighPrice',
        'LowPrice',
        'ClosePrice',
        'Volume',
        'NA'
    ]
)

print(df.head())

df['ClosePrice'].plot(figsize=(14,7))

plt.show()