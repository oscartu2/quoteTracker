from lxml import html
import requests


class Stock():
	
	def __init__(self, symbol, previous_price, current_price):

		self.previous_price = previous_price
		self.current_price = current_price
		self.symbol = symbol
		self.link = 'https://ca.finance.yahoo.com/chart/' + str(self.symbol)
		self.page = requests.get(self.link)
		self.tree = html.fromstring(self.page.content)
		
	def scrape(self):
		print("self.link", self.link)
		self.current_price = self.tree.xpath('//*[@id="chart-header"]/div[2]/div[2]/div/span[1]/text()') # Can't get "current" but can get the one beside it
		print("Before converting to list [0]: ", self.current_price)
		
		self.current_price = float(self.current_price[0].replace(',',''))
		print("Current price: ", self.current_price)
		return self.current_price

	def get_current_price(self):
		return self.current_price

	def get_previous_price(self):
		return self.previous_price

	def get_delta(self):
		return self.current_price - self.previous_price

	def get_delta_close(self):

		d_close = self.tree.xpath('//*[@id="chart-header"]/div[2]/div[2]/div/span[2]/text()') # Where "current price" should be it is this
		if (len(d_close) > 1):
			return d_close[1]
		else:
			return d_close[0]

		return str(d_close[1])

	def get_symbol(self):
		return self.symbol

	def update(self):
		self.previous_price = self.current_price
		self.current_price = self.scrape()

