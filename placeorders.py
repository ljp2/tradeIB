from twsapp import TWSapi, connect, SPYcontract
from orders import *

def placeLongLimitOrder(quantity: int, price: float, transmit=True):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyLimitOrder(quantity, price, transmit=transmit)
    app.placeOrder(oid, SPYcontract(), order)
    app.disconnect()


def placeShortLimitOrder(quantity: int, price: float, transmit=True):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = SellLimitOrder(quantity, price, transmit=transmit)
    app.placeOrder(oid, SPYcontract(), order)
    app.disconnect()


def placeLongMarketOrder(quantity: int, transmit=True):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = BuyMarketOrder(quantity, transmit=transmit)
    app.placeOrder(oid, SPYcontract(), order)
    app.disconnect()


def placeShortMarketOrder(quantity: int, transmit=True):
    app = TWSapi()
    connect(app)
    oid = app.nextOrderId()
    order = SellMarketOrder(quantity, transmit=transmit)
    app.placeOrder(oid, SPYcontract(), order)
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
    app.placeOrder(oid, SPYcontract(), order)
    app.order_filled_event.wait(3)
    print("THE FILLED EVENT is ", app.order_filled_event.is_set())
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

    app.placeOrder(app.nextOrderId(), SPYcontract(), stop_order)
    app.placeOrder(app.nextOrderId(), SPYcontract(), profit_order)

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
    app.placeOrder(oid, SPYcontract(), order)
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

    app.placeOrder(app.nextOrderId(), SPYcontract(), stop_order)
    app.placeOrder(app.nextOrderId(), SPYcontract(), profit_order)

    app.disconnect()

