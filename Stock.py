from lxml import html
import requests
import time


class Stock():
	
	def __init__(self, symbol, interval: float):

		self.previous_price = scrape(symbol)
		time.sleep(interval)
		self.current_price = scrape(symbol)
		
	def scrape(symbol):
		page = requests.get('https://finance.yahoo.com/quote/' + str(symbol))
		tree = html.formstring(page.content)

	def get_current_price(self):
		return self.current_price

	def get_previous_price(self):
		return self.previous_price

	def get_delta(self):
		return self.current_price - self.previous_price

	def update(self):
		self.previous_price = self.current_price
		self.current_price = scrape()

