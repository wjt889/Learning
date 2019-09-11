import json
import requests

gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
symbol = 'btcusd'

btc_data = requests.get(gemini_ticker.format(symbol)).json()
print(json.dumps(btc_data,indent=4))
print(type(json.dumps(btc_data,indent=4)))
dic = eval(json.dumps(btc_data,indent=4))  # src--->dic的转换
print(type(dic)) #查看对象的类型
print(dic['ask'])

