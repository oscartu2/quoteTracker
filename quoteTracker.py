from tkinter import *
from tkinter import messagebox

import Stock
import time
import datetime

class Tracker():

	def __init__(self):
		self.root = Tk()
		self.root.title("Quote Tracker 5000!")

		self.market_select = self.market_select_window_init("Select Market")
		self.markets = ['NYSE', 'TSX']
		self.market_list_var = StringVar()
		self.market_list_var.set(self.markets[0])
		self.market_list = self.market_list_init(self.market_list_var, self.markets)

		self.stocks_list = StringVar()
		self.stocks_list_entry = self.stocks_list_init(self.stocks_list)
		Label(self.root, text="List of stocks").grid(row=4, column=0)

		self.begin_button = self.begin_button_init()

	def stocks_list_init(self, var):
		var.set("")
		e = Entry(self.root, textvariable=var, width=55)
		e.grid(row=4, column=1)
		return e

	def market_select_window_init(self, text):
		market = Text(self.root, height=1, width=70)
		market.grid(row=0, column=0, columnspan=2)
		market.insert(END, text)
		return market

	def market_list_init(self, var, items):
		w = OptionMenu(self.root, var, *items)
		w.grid(row=1, columnspan=2)
		return 2

	def begin_button_init(self):
		button = Button(self.root, text="$$$", command=lambda: self.start())
		button.grid(row=10, columnspan=2)
		return button

	def start(self):
		flag = False
		ticket_symbols = self.stocks_list.get()#input("Please enter the list of ticket symbols separated by a comma that you want to track: ")
		interval = 1 #int(input("Please enter the time interval (in seconds) you wish to check/update the stock: "))
		
		ts = ticket_symbols.strip().split(",")
		ts_dict = {}
		count = 6
		for symbol in ts:
				count += 1
				stock = Stock.Stock(symbol, 0.0, 0.0)
				stock.scrape()
				ts_dict[symbol] = stock
				print("Initializing stock: ", stock.get_stock_name())
				Label(self.root, text=stock.get_stock_name()).grid(row=count, columnspan=2)
				# Add onto GUI: Stock symbol on one side, and delta with red down/green up arrow on other side

		self.root.update()

		while (True): # Implement "stop" button
			time.sleep(interval)
			print('\nThe current time is: ' + str(datetime.datetime.now().time()) + '\n')
			for symbol in ts_dict:
				ts_dict[symbol].update()
				print("Stock: ", ts_dict[symbol].get_stock_name())
				print("Delta display: " + str(ts_dict[symbol].get_delta()))
				print("Delta close: " + str(ts_dict[symbol].get_delta_close()))
				#self.update_buttons() # If prev>curr show red, if prev<curr show green, if prev=curr show = sign
			if (flag):
				break
		print("Program Finished")
		#draw()
		#search()

window = Tracker()
window.root.mainloop()

