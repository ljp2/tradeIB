import time
from tkinter import *
from tkinter import ttk

import placeorders

class GUI(Tk):
    def buyMKTorder(self):
        placeorders.buyMarketOrder(100)

    def sellMKTorder(self):
        placeorders.sellMarketOrder(100)

    def buyLMTorder(self):
        price = self.buy_lim_price.get()
        print("Buy LMT Order @", price)

    def sellLMTorder(self):
        price = self.sell_lim_price.get()
        print("Sell LMT Order @", price)

    def __init__(self):
        super().__init__()
        self.title("TWS Trading")

        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.buy_lim_price = StringVar()
        self.buy_lim_quanity = StringVar()
        self.sell_lim_price = StringVar()
        self.sell_lim_quanity = StringVar()

        self.buy_mkt_quanity = StringVar()
        self.sell_mkt_quanity = StringVar()

        # BUY LMT
        ttk.Button(mainframe, text="Buy\nLMT Order", command=self.buyLMTorder).grid(row=2, column=1, sticky=(W, E))
        buy_lim_quanity_entry = ttk.Entry(mainframe, width=7, textvariable=self.buy_lim_quanity).grid(row=2, column=2)
        buy_lim_price_entry = ttk.Entry(mainframe, width=7, textvariable=self.buy_lim_price).grid(row=2, column=3)

        # SELL LMIT
        ttk.Button(mainframe, text="Sell\nLMT Order", command=self.sellLMTorder).grid(row=2, column=4, sticky=(W, E))
        sell_lim_quanity_entry = ttk.Entry(mainframe, width=7, textvariable=self.sell_lim_quanity).grid(row=2, column=5)
        sell_lim_price_entry = ttk.Entry(mainframe, width=7, textvariable=self.sell_lim_price).grid(row=2, column=6)

        # BUY MKT
        ttk.Button(mainframe, text="Buy\nMKT Order", command=self.buyMKTorder).grid(row=3, column=1, sticky=(W, E))
        buy_mkt_quanity_entry = ttk.Entry(mainframe, width=7, textvariable=self.buy_mkt_quanity).grid(row=3, column=2)

        # SELL MKT
        ttk.Button(mainframe, text="Sell\nMKT Order", command=self.sellMKTorder).grid(row=3, column=4, sticky=(W, E))
        sell_mkt_quanity_entry = ttk.Entry(mainframe, width=7, textvariable=self.sell_mkt_quanity).grid(row=3, column=5)

        # Labels
        ttk.Label(mainframe, text='Quantity').grid(row=1, column=2)
        ttk.Label(mainframe, text='Quantity').grid(row=1, column=5)
        ttk.Label(mainframe, text='Price').grid(row=1, column=3)
        ttk.Label(mainframe, text='Price').grid(row=1, column=6)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)



if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
