import time
from tkinter import *
from tkinter import ttk

import placeorders

class GUI(Tk):
    def buyMKTorder(self):
        print('CLICK')

    def sellMKTorder(self):
        print('CLICK')

    def buyLMTorder(self):
        print('CLICK')

    def sellLMTorder(self):
        print('CLICK')

    def __init__(self):
        super().__init__()
        self.title("TWS Trading")

        self.buy_lim_price = StringVar()
        self.buy_lim_quanity = StringVar()
        self.sell_lim_price = StringVar()
        self.sell_lim_quanity = StringVar()

        self.buy_mkt_quanity = StringVar()
        self.sell_mkt_quanity = StringVar()

        # MKT Frame
        mktframe = ttk.Labelframe(self, text='MKT orders')
        mktframe.grid(row=0, column=0, padx=10, pady=10)
        mktquantlbl = ttk.Label(mktframe, text='Quantity')
        mktquantlbl.grid(row=0, column=1)

        # BUY MKT
        buy_mkt_quanity_btn = ttk.Button(mktframe, text="Buy\nMKT Order", command=self.buyMKTorder)
        buy_mkt_quanity_entry = ttk.Entry(mktframe, width=7, textvariable=self.buy_mkt_quanity)
        buy_mkt_quanity_btn.grid(row=1, column=0, padx=5, pady=5)
        buy_mkt_quanity_entry.grid(row=1, column=1)

        # SELL MKT
        sell_mkt_quanity_btn = ttk.Button(mktframe, text="Sell\nMKT Order", command=self.sellMKTorder)
        sell_mkt_quanity_entry = ttk.Entry(mktframe, width=7, textvariable=self.sell_mkt_quanity)
        sell_mkt_quanity_btn.grid(row=2, column=0, padx=5, pady=5)
        sell_mkt_quanity_entry.grid(row=2, column=1)

        # LMT Frame
        lmtframe = ttk.Labelframe(self, text='LMT orders')
        lmtframe.grid(row=0, column=1, padx=10, pady=10)
        lmtquantlbl = ttk.Label(lmtframe, text='Quantity')
        lmtpricelbl = ttk.Label(lmtframe, text='Price')
        lmtquantlbl.grid(row=0, column=1)
        lmtpricelbl.grid(row=0, column=2)

        # BUY lmt
        buy_lmt_quanity_btn = ttk.Button(lmtframe, text="Buy\nLMT Order", command=self.buyLMTorder)
        buy_lmt_quanity_entry = ttk.Entry(lmtframe, width=7, textvariable=self.buy_mkt_quanity)
        buy_lim_price_entry= ttk.Entry(lmtframe, width=7, textvariable=self.buy_lim_price)
        buy_lmt_quanity_btn.grid(row=1, column=0, padx=5, pady=5)
        buy_lmt_quanity_entry.grid(row=1, column=1)
        buy_lim_price_entry.grid(row=1, column=2)

        # SELL lmt
        sell_lmt_quanity_btn = ttk.Button(lmtframe, text="Sell\nLMT Order", command=self.sellLMTorder)
        sell_lmt_quanity_entry = ttk.Entry(lmtframe, width=7, textvariable=self.sell_lim_quanity)
        sell_lim_price_entry = ttk.Entry(lmtframe, width=7, textvariable=self.sell_lim_price)
        sell_lmt_quanity_btn.grid(row=2, column=0, padx=5, pady=5)
        sell_lmt_quanity_entry.grid(row=2, column=1, padx=5, pady=5)
        sell_lim_price_entry.grid(row=2, column=2, padx=5, pady=5)

        # Bracket Frame
        bracframe = ttk.Labelframe(self, text='Bracket Orders')
        bracframe.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        ttk.Label(bracframe, text="BRACKET FRAME").grid(row=0, column=0)

if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
