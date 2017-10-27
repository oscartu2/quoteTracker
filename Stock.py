from lxml import html
import requests


class Stock():
	
	def __init__(self, symbol, previous_price, current_price):

		self.previous_price = previous_price
		self.current_price = current_price
		self.symbol = symbol
		self.page = requests.get('https://finance.google.ca/finance?q=' + str(self.symbol))
		self.tree = html.fromstring(self.page.content)
		
	def scrape(self):

		self.current_price = self.tree.xpath('//*[@id="ref_22144_l"]/text()') # Can't get "current" but can get the one beside it
		self.current_price = float(self.current_price[0])
		print("Current price: ", self.current_price)
		return self.current_price

	def get_current_price(self):
		return self.current_price

	def get_previous_price(self):
		return self.previous_price

	def get_delta(self):
		return self.current_price - self.previous_price

	def get_delta_close(self):
		d_close_dollar = self.tree.xpath('//*[@id="ref_22144_c"]/text()') # Where "current price" should be it is this
		d_close_dollar = d_close_dollar[0]
		d_close_percent = self.tree.xpath('//*[@id="ref_22144_cp"]/text()')
		d_close_percent = d_close_percent[0]
		return str(d_close_dollar) + ", " + str(d_close_percent)

	def get_symbol(self):
		return self.symbol

	def update(self):
		self.previous_price = self.current_price
		self.current_price = self.scrape()

