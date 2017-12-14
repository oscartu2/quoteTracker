from tkinter import *
from tkinter import messagebox

import Stock
import time
import datetime

class Tracker():

	def __init__(self):
		self.root = Tk()
		self.root.title("Quote Tracker 9000")
		self.flag = True

		self.time_window = self.time_window_init("Time started: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

		self.programs = ['Tracker', 'Info']
		self.program_type_var = StringVar()
		self.program_type_var.set(self.programs[0])
		self.programs_list = self.programs_list_init(self.program_type_var, self.programs)
		Label(self.root, text="Select quote info or quote tracker: ").grid(row=1, column=0, padx=10)

		self.time_interval_var = StringVar()
		self.time_interval_entry = self.time_interval_entry_init(self.time_interval_var)
		Label(self.root, text="Time interval in seconds to update").grid(row=3, column=0, padx=10)

		self.messages_to_user_var = StringVar()
		self.messages_to_user_disp = Label(self.root, textvariable=self.messages_to_user_var, padx=20, fg='red')
		self.messages_to_user_disp.grid(row=5, column=1)

		self.stocks_list = StringVar()
		self.stocks_list_entry = self.stocks_list_init(self.stocks_list)
		Label(self.root, text="List of stocks/Stock to get info").grid(row=4, column=0)
		
		self.stock_space = StringVar()
		self.stock_disp = Label(self.root, textvariable=self.stock_space, padx=20)
		self.stock_disp.grid(row=6, column=0)

		self.current_price = StringVar()
		self.current_disp = Label(self.root, textvariable=self.current_price, width=7)
		self.current_disp.grid(row=6, column=1)

		self.delta_price = StringVar()
		self.delta_disp = Label(self.root, textvariable=self.delta_price, width=7)
		self.delta_disp.grid(row=6, column=2)
		

		self.begin_button = self.begin_button_init(20)
		self.end_button = self.end_button_init(20)

	def init_stock_space(self, row_number, name):
		self.stock_space = StringVar()
		self.stock_disp = Label(self.root, textvariable=self.stock_space, padx=20)
		self.stock_disp.grid(row=row_number, column=0)

	def init_current_price(self, row_number, price):
		self.current_price = StringVar()
		self.current_disp = Label(self.root, textvariable=self.current_price)
		self.current_disp.grid(row=row_number, column=1)
	
	def init_delta_price(self, row_number, price):
		self.delta_price = StringVar()
		self.delta_disp = Label(self.root, textvariable=self.delta_price, fg="green")
		self.delta_disp.grid(row=row_number, column=2)
	
	def set_delta_price(self, price):
		if price >= 0:
			self.delta_disp = Label(self.root, textvariable=price, height=1, fg="green")
			print("delta green")
		else:
			self.delta_disp = Label(self.root, textvariable=price, height=1, fg="red")
			print("delta red")

	def time_interval_entry_init(self, var):
		var.set('1')
		e = Entry(self.root, textvariable=var, width=10)
		e.grid(row=3, column=1, sticky=W)
		return e

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

	def programs_list_init(self, var, items):
		w = OptionMenu(self.root, var, *items)
		w.grid(row=1, column=1, columnspan=1)
		return 2

	def begin_button_init(self, row_number):
		button = Button(self.root, text="Start", command=lambda: self.start())
		button.grid(row=row_number, column=1, sticky=W, pady=15)
		return button

	def end_button_init(self, row_number):
		button = Button(self.root, text="Stop", command=lambda: self.stop())
		button.grid(row=row_number, column=1, pady=15)
		return button

	def write_to_time_window(self, text):
		self.time_window.delete('1.0', END)
		self.time_window.insert(END, text)

	def stop(self):
		self.flag = False
		self.write_to_time_window("Time Stopped: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

	def start(self):
		self.flag = True
		ticket_symbols = self.stocks_list.get()
		interval = int(self.time_interval_var.get())
		ts = ticket_symbols.strip().split(",")
		
		if len(ts) > 1 and (self.program_type_var.get().upper().startswith("I")):
			self.messages_to_user_var.set("You are in INFO mode, either enter one symbol or switch mode!")
			self.root.update()
			return
		elif len(ts) == 1 and (self.program_type_var.get().upper().startswith("I")):
			stock = Stock.Stock(ts, 0.0, 0.0, self.program_type_var.get())
			stock_info = stock.scrape()
			print(stock_info)

		else:
			self.messages_to_user_var.set("You are now in Tracker mode.")
			self.program_type_var.set(self.programs[0])
			if (len(ts)> 15):
				self.messages_to_user_var.set("Please enter <= 15 max stocks to track!")
				self.stocks_list.set(", ".join(ts[:15]))
			else:
				ts_dict = {}
				count = 6
				for symbol in ts:
						count += 1
						stock = Stock.Stock(symbol, 0.0, 0.0, self.program_type_var.get())
						stock.scrape()
						ts_dict[symbol] = stock
						self.init_stock_space(count, stock.get_stock_name())
						self.stock_space.set(stock.get_stock_name())
						self.init_current_price(count, stock.get_current_price())
						self.current_price.set(stock.get_current_price())
						self.init_delta_price(count, '0.0')
						self.delta_price.set('0.0')
						self.root.update()
						
				self.root.update()

				while (self.flag): # Implement "stop" button
					time.sleep(interval)
					self.write_to_time_window("Current time: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
					for symbol in ts_dict:
						ts_dict[symbol].update()
						self.current_price.set(stock.get_current_price())
						self.set_delta_price(stock.get_delta())
						self.root.update()
					if (not self.flag):
						break


window = Tracker()
window.root.mainloop()

