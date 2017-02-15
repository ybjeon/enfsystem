from scrapy.spiders import Spider
#from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from dirbot.items import Website
import random

index = 1
class DmozSpider(Spider):
	name = "ustream"
	allowed_domains = ["ustream.tv"]
	start_urls = [
#		"http://www.ustream.tv/explore/gaming/all?type=live" 
		
		"https://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=2",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=3",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=4",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=5",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=6",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=7",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=8",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=9",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=10",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=11",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=12",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=13",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=14",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=15",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=16",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=17",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=18",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=19",
		"http://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=20",
	
		#"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		#"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
	]


	def parse(self, response):
		"""
		The lines below is a spider contract. For more info see:
		http://doc.scrapy.org/en/latest/topics/contracts.html

		@url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
		@scrapes name
		"""
		"""
		sel = HtmlXPathSelector(response)
		#sites = sel.xpath('//ul[@class="directory-url"]/li')
		sites = sel.xpath('//span[@class="item-location"]/span')
		items = []
		"""
		"""
		for site in sites:
			item = Website()
			item['name'] = site.xpath('a/text()').extract()
			item['url'] = site.xpath('a/@href').extract()
			item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
			items.append(item)
		return items
		"""

		global index

		#filename = response.url.split("/")[-2]
		filename = "../../../googleMap/ver_javascript/data_folder/page"+str(index)
		index = index+1
		with open(filename, 'wb') as f:
			f.write(response.body)
