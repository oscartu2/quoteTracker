from lxml import html
import requests


class Stock():
	
	def __init__(self, symbol, previous_price, current_price, program_type):
		self.program_type = program_type
		self.previous_price = previous_price
		self.current_price = current_price
		self.entered_symbol = str(symbol).strip()
		self.link = 'https://ca.finance.yahoo.com/chart/' + str(self.entered_symbol)
		self.page = requests.get(self.link)
		self.tree = html.fromstring(self.page.content)
		self.stock_name = str(self.tree.xpath('//*[@id="chart-header"]/div[2]/div[1]/div[1]/h1/text()')[0])
		
	def scrape(self):
		self.current_price = self.tree.xpath('//*[@id="chart-header"]/div[2]/div[2]/p/span[1]/text()')
		self.current_price = float(self.current_price[0].replace(',',''))

		if (self.program_type == 'Tracker'):
			return self.current_price
		else:
			info_list = {}
			previous_close = float(self.tree.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]/span/text()'))
			market_cap = float(self.tree.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]/span/text()'))
			beta = float(self.tree.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[2]/span/text()'))
			forward_dividend = float(self.tree.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[6]/td[2]/text()'))
			average_volume = float(self.tree.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]/span/text()'))
			info_list['Current Price: '] = (self.current_price)
			info_list['Previous Close: '] = (previous_close)
			info_list['Market Cap: '] = (market_cap)
			info_list['Beta: '] = (beta)
			info_list['Forward Dividend: '] = (forward_dividend)
			info_list['Average Volume: '] = (average_volume)
			return info_list

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

	def get_stock_name(self):
		return self.stock_name

	def update(self):
		self.previous_price = self.current_price
		self.current_price = self.scrape()

