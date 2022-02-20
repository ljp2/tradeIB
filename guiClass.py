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

        mainframe = ttk.Frame(self, padding="3 3 12 12" )
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        # BUY LMT
        ttk.Button(mainframe, text="Buy\nLMT Order", command=self.buyLMTorder).grid(row=1, column=1, sticky=(W, E))
        self.buy_lim_price = StringVar()
        buy_lim_price_entry = ttk.Entry(mainframe, width=7, textvariable=self.buy_lim_price).grid(row=1, column=2)

        # SELL LMIT
        ttk.Button(mainframe, text="Sell\nLMT Order", command=self.sellLMTorder).grid(row=1, column=3, sticky=(W, E))
        self.sell_lim_price = StringVar()
        sell_lim_price_entry = ttk.Entry(mainframe, width=7, textvariable=self.sell_lim_price).grid(row=1, column=5)

        # BUY MKT
        ttk.Button(mainframe, text="Buy\nMKT Order", command=self.buyMKTorder).grid(row=2, column=1, sticky=(W, E))

        # SELL MKT
        ttk.Button(mainframe, text="Sell\nMKT Order", command=self.sellMKTorder).grid(row=2, column=3, sticky=(W, E))


        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)



if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
