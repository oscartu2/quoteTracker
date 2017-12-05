import tkinter
#import tkMessageBox
import Stock
import time
import datetime


def refresh(interval):
	# Updates the stocks and direction of the pricing with red/green arrows
	# for every specified interval of time
	print("test")

def draw():
	# Draw the GUI?
	# GUI: Displays a list of stock symbols with current price, previous price, 
	# and direction it has gone (up or down) since last refresh. 
	# Possible also to show refreshed X times since launch, and other logistics.
	print("test draw")

def update_buttons():
	print("update buttons\n")

def main():
	flag = False
	ticket_symbols = input("Please enter the list of ticket symbols separated by a comma that you want to track: ")
	interval = int(input("Please enter the time interval (in seconds) you wish to check/update the stock: "))
	ts = ticket_symbols.strip().split(",")
	ts_dict = {}
	for symbol in ts:
			stock = Stock.Stock(symbol, 0.0, 0.0)
			stock.scrape()
			time.sleep(interval)
			stock.update()
			ts_dict[symbol] = stock
			delta = stock.get_delta()
			print("Initializing stock: ", stock.get_stock_name())
			print("Delta from last time we displayed: ", delta)
			delta_close = stock.get_delta_close()
			print("Delta from previous close: ", delta_close)
			# Add onto GUI: Stock symbol on one side, and delta with red down/green up arrow on other side

	while (True): # Implement "stop" button
		time.sleep(interval)
		print('\nThe current time is: ' + str(datetime.datetime.now().time()) + '\n')
		for symbol in ts_dict:
			ts_dict[symbol].update()
			print("Stock: ", ts_dict[symbol].get_stock_name())
			print("Delta display: " + str(ts_dict[symbol].get_delta()))
			print("Delta close: " + str(ts_dict[symbol].get_delta_close()))
			update_buttons() # If prev>curr show red, if prev<curr show green, if prev=curr show = sign
		if (flag):
			break
	print("Program Finished")
	#draw()
	#search()
'''
top = Tkinter.Tk()
# Code to add widgets will go here...

top.minsize(width=420, height=420)

B = Tkinter.Button(top, text="hello")
B.pack()

top.mainloop()
'''

if __name__ == "__main__":
	main()
