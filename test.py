import time
import pyupbit
import datetime
import requests

access = ""
secret = ""
myToken = ""

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma15(ticker):
    """15일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
    ma15 = df['close'].rolling(15).mean().iloc[-1]
    return ma15

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# 시작 메세지 슬랙 전송
post_message(myToken,"#bitcoin", "autotrade start")
count = [0,0,0,0,0]

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            #btc
            target_price_btc = get_target_price("KRW-BTC", 0.5)
            ma15_btc = get_ma15("KRW-BTC")
            current_price_btc = get_current_price("KRW-BTC")
            krw = krw = get_balance("KRW")
            if target_price_btc < current_price_btc and ma15_btc < current_price_btc and count[0] == 0:
                count[0] = count[0] + 1
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-BTC", krw*0.9995/(5))
                    post_message(myToken,"#bitcoin", "BTC buy : " +str(buy_result))
            #eth
            target_price_eth = get_target_price("KRW-ETH", 0.5)
            ma15_eth = get_ma15("KRW-ETH")
            current_price_eth = get_current_price("KRW-ETH")
            if target_price_eth < current_price_eth and ma15_eth < current_price_eth and count[1] == 0:
                count[1] = count[1] + 1
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ETH", krw*0.9995/(5))
                    post_message(myToken,"#bitcoin", "ETH buy : " +str(buy_result))
            #doge
            target_price_doge = get_target_price("KRW-DOGE", 0.5)
            ma15_doge = get_ma15("KRW-DOGE")
            current_price_doge = get_current_price("KRW-DOGE")
            if target_price_doge < current_price_doge and ma15_doge < current_price_doge and count[2] == 0:
                count[2] = count[2] + 1
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-DOGE", krw*0.9995/(5))
                    post_message(myToken,"#bitcoin", "DOGE buy : " +str(buy_result))
            #xrp
            target_price_XRP = get_target_price("KRW-XRP", 0.5)
            ma15_XRP = get_ma15("KRW-XRP")
            current_price_XRP = get_current_price("KRW-XRP")
            if target_price_XRP < current_price_XRP and ma15_XRP < current_price_XRP and count[3] == 0:
                count[3] = count[3] + 1
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-XRP", krw*0.9995/(5))
                    post_message(myToken,"#bitcoin", "XRP buy : " +str(buy_result))
            #ada
            target_price_ADA = get_target_price("KRW-ADA", 0.5)
            ma15_ADA = get_ma15("KRW-ADA")
            current_price_ADA = get_current_price("KRW-ADA")
            if target_price_ADA < current_price_ADA and ma15_ADA < current_price_ADA and count[4] == 0:
                count[4] = count[4] + 1
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-ADA", krw*0.9995/(5))
                    post_message(myToken,"#bitcoin", "ADA buy : " +str(buy_result))
        else:
            count = [0,0,0,0,0]
            #btc
            btc = get_balance("BTC")
            if btc > 0.00008:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#bitcoin", "BTC buy : " +str(sell_result))
            #eth
            eth = get_balance("ETH")
            if eth > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                post_message(myToken,"#bitcoin", "ETH buy : " +str(sell_result))
            #doge
            doge = get_balance("DOGE")
            if doge > 0.00008:
                sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                post_message(myToken,"#bitcoin", "DOGE buy : " +str(sell_result))
            #xrp
            xrp = get_balance("XRP")
            if xrp > 0.00008:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                post_message(myToken,"#bitcoin", "XRP buy : " +str(sell_result))
            #ADA
            ada = get_balance("ADA")
            if ada > 0.00008:
                sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                post_message(myToken,"#bitcoin", "ADA buy : " +str(sell_result))
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#bitcoin", e)
        time.sleep(1)