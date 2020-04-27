# weather_hack.py
#   Livedorreお天気Webサービス Weather Hacks用クライアントコマンド
#   Usage: weather_hack.py city_id
#
import argparse
import sys
import urllib.request, urllib.parse
import json
import city_id_data

# Weather Hacks URL
WH_URL = 'http://weather.livedoor.com/forecast/webservice/json/v1?'

# コマンド引数取得
def get_cmd_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("city_name", type=str)
    args = parser.parse_args()
    return(args)

# 都市名からCity IDを取得
def get_city_id(city_name):
    return(city_id_data.city_id_dict[city_name])

# お天気情報出力
def print_weather(data):
    # 都市名
    print(data['location']['prefecture'], data['location']['city'])
    # お天気概況
    print(data['description']['text'])
    # 日毎のお天気情報
    for forecast in data['forecasts']:
        print(forecast['dateLabel'])
        print('\t',forecast['telop'])
        if forecast['temperature']:
            if forecast['temperature']['min']:
                if forecast['temperature']['min']['celsius']:
                    print("\t  最低温度 ", forecast['temperature']['min']['celsius'],'°C')
            if forecast['temperature']['max']:
                if forecast['temperature']['max']['celsius']:
                    print("\t  最高温度 ", forecast['temperature']['max']['celsius'],'°C')

# メイン
args = get_cmd_arg()
# 都市名がしていされているかチェック
try:
    city_name = args.city_name
except:
    print("usage: weather_hack.py city_name", file=sys.stderr)
    sys.exit(-1)

# City ID取得
city_id = get_city_id(city_name)
if city_id == None:
    print("id for ", city_name, " is not found", file=sys.stderr)
    sys.exit(-1)

# URLクエリストリング設定
params = {
    "city": city_id
}
# URLエンコード
p = urllib.parse.urlencode(params)
url = WH_URL + p

# HTTPリクエスト送信
weather_info = {}
with urllib.request.urlopen(url) as res:
    json_data = json.load(res)

# お天気情報出力
print_weather(json_data)