from ibapi.client import EClient
from ibapi.common import TickerId, TickAttrib
from ibapi.ticktype import TickType, TickTypeEnum
from ibapi.utils import floatMaxString
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import threading


class TWSapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.nextValidOrderId = None
        self.event_connect = threading.Event()
        self.event_reqMktData = threading.Event()

        self.order_filled_event = threading.Event()
        self.order_filled_event.clear()

        self.active_oid: int = None
        self.active_quantity: int = None
        self.active_fill_price: float = None
        self.current_price = None

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
            print("SET THE EVENT")
        else:
            print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining,
                  'lastFillPrice', lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.sharets, execution.lastLiquidity)

    def tickPrice(self, reqId: TickerId, tickType: TickType, price: float,
                  attrib: TickAttrib):
        super().tickPrice(reqId, tickType, price, attrib)
        # print("TickPrice. TickerId:", reqId, "tickType:", tickType,
        #       "Price:", floatMaxString(price), "CanAutoExecute:", attrib.canAutoExecute,
        #       "PastLimit:", attrib.pastLimit, end=' ')
        # if tickType == TickTypeEnum.BID or tickType == TickTypeEnum.ASK:
        #     print("PreOpen:", attrib.preOpen)
        # else:
        #     print()
        if tickType == TickTypeEnum.LAST:
            self.current_price = price


    def tickSnapshotEnd(self, reqId: int):
        super().tickSnapshotEnd(reqId)
        self.event_reqMktData.set()


def SPYcontract():
    contract = Contract()
    contract.symbol = 'SPY'
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = 'USD'
    return contract


def connect(app: TWSapi):
    app.connect('127.0.0.1', 7497, 123)
    app.nextorderId = None
    api_thread = threading.Thread(target=app.run, daemon=True)
    api_thread.start()
    app.event_connect.wait()


def getCurrentPrice():
    app = TWSapi()
    connect(app)
    app.event_reqMktData.clear()
    app.reqMktData(1000, SPYcontract(), "", True, False, [])
    app.event_reqMktData.wait()
    app.disconnect()
    # print('Current Price =', app.current_price)
    return app.current_price

if __name__ == '__main__':
    print( getCurrentPrice() )
