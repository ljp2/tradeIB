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


def connect(app: TWSapi):
    app.connect('127.0.0.1', 7497, 123)
    app.nextorderId = None
    api_thread = threading.Thread(target=app.run, daemon=True)
    api_thread.start()
    app.event_connect.wait()


def placeLongLimitOrder(quantity: int, price: float, transmit=True):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyLimitOrder(quantity, price, transmit=transmit)
    app.placeOrder(oid, contract, order)
    app.disconnect()


def placeShortLimitOrder(quantity: int, price: float, transmit=True):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = SellLimitOrder(quantity, price,transmit=transmit)
    app.placeOrder(oid, contract, order)
    app.disconnect()


def placeLongMarketOrder(quantity: int, transmit=True):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyMarketOrder(quantity, transmit=transmit)
    app.placeOrder(oid, contract, order)
    app.disconnect()


def placeShortMarketOrder(quantity: int, transmit=True):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = SellMarketOrder(quantity, transmit=transmit)
    app.placeOrder(oid, contract, order)
    app.disconnect()


def placeLongBracketOrder(quantity: int):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyMarketOrder(quantity, transmit=True)

    app.active_oid = oid
    app.active_quantity = quantity
    app.active_fill_price = None
    app.order_filled_event.clear()
    app.placeOrder(oid, contract, order)
    # app.order_filled_event.wait()
    fill_price = app.active_fill_price

    print("ORDER FILLED @ ", fill_price)

    profit_price = fill_price +  0.50
    stop_price = fill_price - 0.50

    # profit_order_id = app.nextOrderId()
    # profit_order = SellLimitOrder(quantity, profit_price, transmit=False)
    # app.placeOrder(profit_order_id, contract, profit_order)

    app.disconnect()

def placeShortBracketOrder(quantity: int):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyMarketOrder(quantity, transmit=True)

    app.active_oid = oid
    app.active_quantity = quantity
    app.active_fill_price = None
    app.order_filled_event.clear()
    app.placeOrder(oid, contract, order)
    app.order_filled_event.wait()
    fill_price = app.active_fill_price

    print("ORDER FILLED @ ", fill_price)

    orders = BracketOrdersForLong(oid, quantity, fill_price)

    for order in orders:
        app.placeOrder(app.nextOrderId(), contract, order)

    # profit_order_id = app.nextOrderId()
    # profit_order = SellLimitOrder(quantity, profit_price, transmit=False)
    # app.placeOrder(profit_order_id, contract, profit_order)

    app.disconnect()

if __name__ == '__main__':
    placeLongMarketOrder(100)
    time.sleep(1)
    placeShortMarketOrder()


