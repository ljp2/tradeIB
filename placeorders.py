import orders
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




def placeLongMKTplusBracketOrder(quantity: int):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyMarketOrder(quantity, transmit=True)

    app.active_oid = oid
    app.active_quantity = quantity
    app.active_fill_price = None
    app.order_filled_event.clear()
    app.placeOrder(oid, contract, order)
    app.order_filled_event.wait(3)
    print("THE FILLED EVENT is ",  app.order_filled_event.is_set())
    fill_price = app.active_fill_price

    print("ORDER FILLED @ ", fill_price)

    profit_price = fill_price + 0.2
    stop_price = fill_price - 0.2

    profit_order = Order()
    profit_order.action = "SELL"
    profit_order.orderType = "LMT"
    profit_order.totalQuantity = quantity
    profit_order.lmtPrice = profit_price

    stop_order = Order()
    stop_order.action = 'SELL'
    stop_order.totalQuantity = quantity
    stop_order.orderType = 'STP'
    stop_order.auxPrice = stop_price

    ocaGroup = "OCA_" + str(oid)
    profit_order.ocaGroup = ocaGroup
    profit_order.ocaType = 2
    stop_order.ocaGroup = ocaGroup
    stop_order.ocaType = 2

    app.placeOrder(app.nextOrderId(), contract, stop_order)
    app.placeOrder(app.nextOrderId(), contract, profit_order)

    app.disconnect()














def placeShortMKTplusBracketOrder(quantity: int):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = SellMarketOrder(quantity, transmit=True)

    app.active_oid = oid
    app.active_quantity = quantity
    app.active_fill_price = None
    app.order_filled_event.clear()
    app.placeOrder(oid, contract, order)
    app.order_filled_event.wait()
    fill_price = app.active_fill_price

    print("ORDER FILLED @ ", fill_price)

    profit_price = fill_price - 0.2
    stop_price = fill_price + 0.2

    profit_order = Order()
    profit_order.action = "BUY"
    profit_order.orderType = "LMT"
    profit_order.totalQuantity = quantity
    profit_order.lmtPrice = profit_price

    stop_order = Order()
    stop_order.action = 'BUY'
    stop_order.totalQuantity = quantity
    stop_order.orderType = 'STP'
    stop_order.auxPrice = stop_price

    ocaGroup = "OCA_" + str(oid)
    profit_order.ocaGroup = ocaGroup
    profit_order.ocaType = 2
    stop_order.ocaGroup = ocaGroup
    stop_order.ocaType = 2

    app.placeOrder(app.nextOrderId(), contract, stop_order)
    app.placeOrder(app.nextOrderId(), contract, profit_order)

    app.disconnect()

if __name__ == '__main__':
    placeLongMarketOrder(100)
    time.sleep(1)
    placeShortMarketOrder()


