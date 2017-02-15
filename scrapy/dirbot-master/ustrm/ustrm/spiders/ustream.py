from scrapy.spiders import Spider
#from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from dirbot.items import Website
import random

index = 1
class DmozSpider(Spider):
	name = "ustream"
	allowed_domains = ["ustream.tv"]
	start_urls = []
#		"http://www.ustream.tv/explore/gaming/all?type=live" 
	for n in range(1, 100):
		start_urls.append("https://www.ustream.tv/ajax-alwayscache/explore/gaming/all.json?subCategory=&type=live&location=anywhere&page=" + str(n))
		start_urls.append("https://www.ustream.tv/ajax-alwayscache/explore/animals/all.json?subCategory=&type=no-offline&location=anywhere&page=" + str(n))
		#start_urls.append("https://www.ustream.tv/ajax-alwayscache/explore/education/all.json?subCategory=&type=live&location=anywhere&page=" + str(n))
		#start_urls.append("https://www.ustream.tv/ajax-alwayscache/explore/spirituality/all.json?subCategory=&type=live&location=anywhere&page=" + str(n))
		#start_urls.append("https://www.ustream.tv/ajax-alwayscache/explore/music/all.json?subCategory=&type=live&location=anywhere&page=" + str(n))
		#start_urls.append("https://www.ustream.tv/ajax-alwayscache/explore/all/all.json?subCategory=&type=live&location=anywhere&page=" + str(n))
	
		#"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		#"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
	


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
		filename = "../../../ver_javascript/data_folder/page"+str(index)
		index = index+1
		with open(filename, 'wb') as f:
			f.write(response.body)
