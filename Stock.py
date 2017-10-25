from lxml import html
import requests


class Stock():
	
	def __init__(self, symbol, previous_price, current_price):

		self.previous_price = previous_price
		self.current_price = current_price
		self.symbol = symbol
		self.page = requests.get('https://finance.yahoo.com/quote/' + str(self.symbol))
		self.tree = html.fromstring(self.page.content)
		
	def scrape(self):

		self.current_price = self.tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/p/span[1]/text()') # Can't get "current" but can get the one beside it
		print(self.current_price)
		
		self.current_price = float(self.current_price[0])
		print(self.current_price)
		return self.current_price

	def get_current_price(self):
		return self.current_price

	def get_previous_price(self):
		return self.previous_price

	def get_delta(self):
		return self.current_price - self.previous_price

	def get_delta_close(self):
		d_close = self.tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()') # Where "current price" should be it is this
		d_close = str(d_close)
		return d_close

	def get_symbol(self):
		return self.symbol
		
	def update(self):
		self.previous_price = self.current_price
		self.current_price = self.scrape()

