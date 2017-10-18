import Tkinter
import tkMessageBox


def refresh(interval):
	# Updates the stocks and direction of the pricing with red/green arrows
	# for every specified interval of time
	print("test")


def search():
	# Automatically webscrape stock information 
	# tkMessageBox.showinfo("Hello Python", "Hello World")

def draw():
	# Draw the GUI?
	# GUI: Displays a list of stock symbols with current price, previous price, 
	# and direction it has gone (up or down) since last refresh. 
	# Possible also to show refreshed X times since launch, and other logistics.
	print("test draw")

def update_buttons():
	print("update btutons")

def main():
	ticket_symbols = input("Please enter the list of ticket symbols separated by a comma that you want to track: ")
	interval = input("Please enter the time interval (in seconds) you wish to check/update the stock: ")
	ts = ticket_symbols.strip().split(",")
	ts_dict = {}
	for symbol in ts:
			stock = Stock(symbol, float(interval))
			ts_dict[symbol] = stock
			delta = stock.get_delta()
			# Add onto GUI: Stock symbol on one side, and delta with red down/green up arrow on other side

	while (True): # Implement "stop" button
		for symbol in ts_dict:
			ts_dict[symbol].update()
			update_buttons() # If prev>curr show red, if prev<curr show green, if prev=curr show = sign
	
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

#if __name__ == "__main__":
	#main()
