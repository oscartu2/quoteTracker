from lxml import html
import requests


class Stock():
	
	def __init__(self, symbol, previous_price, current_price):

		self.previous_price = previous_price
		self.current_price = current_price
		self.symbol = symbol
		
	def scrape(self):
		page = requests.get('https://finance.yahoo.com/quote/' + str(self.symbol))
		tree = html.fromstring(page.content)

		# Probably the current_price. Will need to debug
		self.current_price = tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')
		print(self.current_price)

	def get_current_price(self):
		return self.current_price

	def get_previous_price(self):
		return self.previous_price

	def get_delta(self):
		return self.current_price - self.previous_price

	def update(self):
		self.previous_price = self.current_price
		self.current_price = scrape()

