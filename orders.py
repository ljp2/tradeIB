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

