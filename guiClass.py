import time
from tkinter import *
from tkinter import ttk

import placeorders


class GUI(Tk):
    def longMKTorder(self):
        quantity = int(self.long_mkt_quantity.get())
        placeorders.placeLongMarketOrder(quantity)

    def shortMKTorder(self):
        quantity = int(self.short_mkt_quantity.get())
        placeorders.placeShortMarketOrder(quantity)

    def longLMTorder(self):
        quantity = int(self.long_lim_quantity.get())
        price = float( self.long_lim_price.get() )
        placeorders.placeLongLimitOrder(quantity, price)

    def shortLMTorder(self):
        quantity = int(self.short_lim_quantity.get())
        price = float( self.short_lim_price.get() )
        placeorders.placeShortLimitOrder(quantity, price)

    def longMKTplusBracketOrder(self):
        quantity = int(self.long_bracket_quantity.get())
        placeorders.placeLongMKTplusBracketOrder(quantity)

    def shortMKTplusBracketOrder(self):
        quantity = int(self.short_bracket_quantity.get())
        placeorders.placeShortMKTplusBracketOrder(quantity)


    def __init__(self):
        super().__init__()
        self.title("TWS Trading")

        # MKT Frame
        mktframe = ttk.Labelframe(self, text='MKT orders')
        mktframe.grid(row=0, column=0, padx=10, pady=10)
        mkt_quantity_lbl = ttk.Label(mktframe, text='Quantity')
        mkt_quantity_lbl.grid(row=0, column=1)
        self.long_mkt_quantity = StringVar(value=100)
        self.short_mkt_quantity = StringVar(value=100)

        # LONG MKT
        long_mkt_quantity_btn = ttk.Button(mktframe, text="Long MKT Order", command=self.longMKTorder)
        # long_mkt_quantity_entry = ttk.Entry(mktframe, width=4, textvariable=self.long_mkt_quantity)
        long_mkt_quantity_entry = ttk.Spinbox(
            mktframe,
            textvariable=self.long_mkt_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        long_mkt_quantity_btn.grid(row=1, column=0, padx=5, pady=5)
        long_mkt_quantity_entry.grid(row=1, column=1)

        # SHORT MKT
        short_mkt_quantity_btn = ttk.Button(mktframe, text="Short MKT Order", command=self.shortMKTorder)
        short_mkt_quantity_entry = ttk.Spinbox(
            mktframe,
            textvariable=self.short_mkt_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        short_mkt_quantity_btn.grid(row=2, column=0, padx=5, pady=5)
        short_mkt_quantity_entry.grid(row=2, column=1)

        # LMT Frame
        self.long_lim_price = StringVar()
        self.long_lim_quantity = StringVar(value=100)
        self.short_lim_price = StringVar(value=0)
        self.short_lim_quantity = StringVar(value=100)

        lmtframe = ttk.Labelframe(self, text='LMT orders')
        lmtframe.grid(row=0, column=1, padx=10, pady=10)
        lmtquantlbl = ttk.Label(lmtframe, text='Quantity')
        lmtpricelbl = ttk.Label(lmtframe, text='Price')
        lmtquantlbl.grid(row=0, column=1)
        lmtpricelbl.grid(row=0, column=2)

        # LONG LMT
        long_lmt_quantity_btn = ttk.Button(lmtframe, text="Long LMT Order", command=self.longLMTorder)
        long_lmt_quantity_entry = ttk.Spinbox(
            lmtframe,
            textvariable=self.long_lim_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        long_lim_price_entry = ttk.Spinbox(
            lmtframe,
            from_= 0,
            to=1000,
            increment=0.5,
            textvariable=self.long_lim_price,
            width=7
        )
        long_lmt_quantity_btn.grid(row=1, column=0, padx=5, pady=5)
        long_lmt_quantity_entry.grid(row=1, column=1)
        long_lim_price_entry.grid(row=1, column=2)

        # SHORT LMT
        short_lmt_quantity_btn = ttk.Button(lmtframe, text="Short LMT Order", command=self.shortLMTorder)
        short_lmt_quantity_entry = ttk.Spinbox(
            lmtframe,
            textvariable=self.short_lim_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        short_lim_price_entry = ttk.Entry(lmtframe, width=7, textvariable=self.short_lim_price)
        short_lmt_quantity_btn.grid(row=2, column=0, padx=5, pady=5)
        short_lmt_quantity_entry.grid(row=2, column=1, padx=5, pady=5)
        short_lim_price_entry.grid(row=2, column=2, padx=5, pady=5)

        # Bracket Frame

        self.long_bracket_quantity = StringVar(value=100)
        self.long_bracket_plus_price_increment = StringVar(value=0.50)
        self.long_bracket_minus_price_increment = StringVar(value=0.50)
        self.short_bracket_quantity = StringVar(value=100)
        self.short_bracket_plus_price_increment = StringVar(value=0.50)
        self.short_bracket_minus_price_increment = StringVar(value=0.50)

        bracframe = ttk.Labelframe(self, text='Bracket Orders')
        bracframe.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        brac_quantity_lbl = ttk.Label(bracframe, text='Quantity').grid(row=0, column=1)
        brac_plus_lbl = ttk.Label(bracframe, text='Positive Increment').grid(row=0, column=2)
        brac_minus_lbl = ttk.Label(bracframe, text='Negative Increment').grid(row=0, column=3)

        # Long Bracket
        long_bracket_btn = ttk.Button(bracframe, text="MKT Long + Bracket Order", command=self.longMKTplusBracketOrder)
        long_bracket_quantity_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.long_bracket_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        long_bracket_plus_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.long_bracket_plus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        long_bracket_minus_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.long_bracket_minus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        long_bracket_btn.grid(row=1, column=0, padx=5, pady=5)
        long_bracket_quantity_entry.grid(row=1, column=1)
        long_bracket_plus_entry.grid(row=1, column=2)
        long_bracket_minus_entry.grid(row=1, column=3)

        # Short Bracket
        short_bracket_btn = ttk.Button(bracframe, text="MKT Short + Bracket Order", command=self.shortMKTplusBracketOrder)
        short_bracket_quantity_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.short_bracket_quantity,
            value=[100, 200, 300, 400],
            width=4
        )
        short_bracket_quantity_entry.grid(row=2, column=1)
        short_bracket_plus_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.short_bracket_plus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        short_bracket_minus_entry = ttk.Spinbox(
            bracframe,
            textvariable=self.short_bracket_minus_price_increment,
            from_=0.20,
            to=2.00,
            increment=0.05,
            width=7
        )
        short_bracket_btn.grid(row=2, column=0, padx=5, pady=5)
        short_bracket_plus_entry.grid(row=2, column=2)
        short_bracket_minus_entry.grid(row=2, column=3)


        # Current  Price
        self.current_price = StringVar(value="Current Price")
        current_price_lbl = ttk.Label(self, width=7, padding=10, textvariable=self.current_price )
        current_price_lbl.grid(row = 2, column=0)


        # for child in self.winfo_children():
        #     child.padx = 10
        #     child.pady = 10


if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()
