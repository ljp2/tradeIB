from ibapi.client import EClient
from ibapi.wrapper import EWrapper

import threading

class TWSapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.nextValidOrderId = None
        self.event_connect = threading.Event()
        self.event_connect.clear()

        self.order_filled_event = threading.Event()
        self.order_filled_event.clear()

        self.active_oid: int = None
        self.active_quantity: int = None
        self.active_fill_price: float = None

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextValidOrderId = orderId
        self.event_connect.set()

        print("NextValidId:", orderId)

    def nextOrderId(self):
        oid = self.nextValidOrderId
        self.nextValidOrderId += 1
        return oid

    def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        if orderId == self.active_oid and filled == int(self.active_quantity):

            self.order_filled_event.set()
            self.active_fill_price = lastFillPrice
            print ("SET THE EVENT")
        else:
            print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining,
                  'lastFillPrice', lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)

