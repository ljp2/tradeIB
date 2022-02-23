from ibapi.order import Order


def LimitOrder(action: str, quantity: int, limitPrice: float, transmit=True):
    order = Order()
    order.action = action
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    order.transmit = transmit
    return order


def MarketOrder(action: str, quantity: int, transmit=True):
    order = Order()
    order.action = action
    order.orderType = "MKT"
    order.totalQuantity = quantity
    order.transmit = transmit
    return order


def BuyLimitOrder(quantity: int, limitPrice: float, transmit=True):
    return LimitOrder('BUY', quantity, limitPrice, transmit=transmit)


def SellLimitOrder(quantity: int, limitPrice: float, transmit=True):
    return LimitOrder('SELL', quantity, limitPrice, transmit=transmit)


def BuyMarketOrder(quantity: int, transmit=True):
    return MarketOrder('BUY', quantity, transmit=transmit)


def SellMarketOrder(quantity: int, transmit=True):
    return MarketOrder('SELL', quantity, transmit=transmit)

def BracketOrdersForLong(parent_oid:int, quantity:int, fill_price:float):
    profit_price = fill_price -  0.50
    stop_price = fill_price + 0.50
    orders = []

    profit_order = Order()
    profit_order.action = "SELL"
    profit_order.orderType = "LMT"
    profit_order.totalQuantity = quantity
    profit_order.lmtPrice = profit_price
    profit_order.transmit = True
    profit_order.parentId = parent_oid
    orders.append(profit_order)

    stop_order = Order()
    stop_order.action = 'SELL'
    stop_order.totalQuantity = quantity
    stop_order.orderType = 'STP'
    stop_order.auxPrice = stop_price
    stop_order.parentId = parent_oid
    stop_order.transmit = True
    orders.append(stop_order)

    return orders