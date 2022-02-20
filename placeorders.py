from twsapp import TWSapi
from orders import *

from ibapi.contract import Contract

import threading
import time

contract = Contract()
contract.symbol = 'SPY'
contract.secType = 'STK'
contract.exchange = 'SMART'
contract.currency = 'USD'



def connect(app:TWSapi):
    app.connect('127.0.0.1', 7497, 123)
    app.nextorderId = None
    api_thread = threading.Thread(target=app.run, daemon=True)
    api_thread.start()
    app.event_connect.wait()


def buyLimitOrder(quantity:int, price:float):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyLimitOrder(quantity, price)
    app.placeOrder(oid, contract, order)
    app.disconnect()

def sellLimitOrder(quantity:int, price:float):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = SellLimitOrder(quantity, price)
    app.placeOrder(oid, contract, order)
    app.disconnect()

def buyMarketOrder(quantity:int):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyMarketOrder(quantity)
    app.placeOrder(oid, contract, order)
    app.disconnect()

def sellMarketOrder(quantity:int):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = SellMarketOrder(quantity)
    app.placeOrder(oid, contract, order)
    app.disconnect()




if __name__ == '__main__':
    buyMarketOrder(100)
    time.sleep(1)
    sellMarketOrder()