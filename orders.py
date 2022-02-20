from ibapi.order import Order


def LimitOrder(action: str, quantity: int, limitPrice: float):
    order = Order()
    order.action = action
    order.orderType = "LMT"
    order.totalQuantity = quantity
    order.lmtPrice = limitPrice
    return order


def MarketOrder(action: str, quantity: int):
    order = Order()
    order.action = action
    order.orderType = "MKT"
    order.totalQuantity = quantity
    return order


def BuyLimitOrder(quantity: int, limitPrice: float):
    return LimitOrder('BUY', quantity, limitPrice)


def SellLimitOrder(quantity: int, limitPrice: float):
    return LimitOrder('SELL', quantity, limitPrice)


def BuyMarketOrder(quantity: int):
    return MarketOrder('BUY', quantity)


def SellMarketOrder(quantity: int):
    return MarketOrder('SELL', quantity)
