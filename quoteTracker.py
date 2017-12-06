from tkinter import *
from tkinter import messagebox

import Stock
import time
import datetime

class Tracker():

	def __init__(self):
		self.root = Tk()
		self.root.title("Quote Tracker 5000!")

		self.time_window = self.time_window_init("Time started: " + str(datetime.datetime.now().time()))

		self.markets = ['NYSE', 'TSX']
		self.market_list_var = StringVar()
		self.market_list_var.set(self.markets[0])
		self.market_list = self.market_list_init(self.market_list_var, self.markets)
		Label(self.root, text="Select a market: ").grid(row=1, column=0)

		self.stocks_list = StringVar()
		self.stocks_list_entry = self.stocks_list_init(self.stocks_list)
		Label(self.root, text="List of stocks").grid(row=4, column=0)

		self.init_stock_space(6, "Initialized stocks will go here")
		self.init_current_price(6, "0.0")
		self.init_delta_price(6, "0.0")

		self.begin_button = self.begin_button_init()

	def init_stock_space(self, row_number, name):
		self.stock_space = StringVar()
		self.stock_disp = Label(self.root, text=name, height=1, width=15)
		self.stock_disp.grid(row=row_number, column=0, columnspan=2)

	def init_current_price(self, row_number, price):
		self.current_price = StringVar()
		self.current_price.set(price)
		self.current_disp = Label(self.root, textvariable='Current Price: ' + str(price), height=1, width=15)
		self.current_disp.grid(row=row_number, column=0, columnspan=2)
	
	def init_delta_price(self, row_number, price):
		self.delta_price = StringVar()
		self.delta_price.set(price)
		self.delta_disp = Label(self.root, textvariable='Delta Price: ' + str(price), height=1, width=15)
		self.delta_disp.grid(row=row_number, column=0, columnspan=2)
		
	

	def stocks_list_init(self, var):
		var.set("")
		e = Entry(self.root, textvariable=var, width=55)
		e.grid(row=4, column=1, columnspan=1)
		return e

	def time_window_init(self, text):
		t = Text(self.root, height=1, width=70)
		t.grid(row=0, column=1, columnspan=1)
		t.insert(END, text)
		return t

	def market_list_init(self, var, items):
		w = OptionMenu(self.root, var, *items)
		w.grid(row=1, column=1, columnspan=1)
		return 2

	def begin_button_init(self):
		button = Button(self.root, text="$$$", command=lambda: self.start())
		button.grid(row=10, columnspan=2)
		return button


	def write_to_time_window(self, text):
		self.time_window.delete('1.0', END)
		self.time_window.insert(END, text)

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
				self.init_stock_space(count, stock.get_stock_name())
				#self.stock_space.set(stock.get_stock_name())
				self.init_current_price(count, stock.get_current_price())
				#self.current_price.set(stock.get_current_price())
				self.init_delta_price(count, '0.0')
				#self.delta_price.set('0.0')
				self.root.update()
				# Add onto GUI: Stock symbol on one side, and delta with red down/green up arrow on other side

		self.root.update()

		while (True): # Implement "stop" button
			time.sleep(interval)
			self.write_to_time_window(str(datetime.datetime.now().time()))
			for symbol in ts_dict:
				ts_dict[symbol].update()

				self.root.update()
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

