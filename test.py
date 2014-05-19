from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractorfrom
from scraper.items import ILGAitems

class ILGAspider(CrawlSpider):
    name = "ilga_leg"
    allowed_domains = ["ilga.gov"]
    start_urls = [
		"http://www.ilga.gov/house/",
		"http://www.ilga.gov/senate/"
    ]
	rule1 = (Rule (SgmlLinkExtractor(allow=('Bills/.asp' ),restrict_xpaths=(‘//table/tbody/tr/td/a,)), follow= True),)
	rule2=  (Rule (SgmlLinkExtractor(allow=('Primary/=True' ), callback=’parse_item’, follow= True),)
	def parse_item(self, response):
		hxs = HtmlXpathSelector(response)
		site = hxs.select('//table[2]/tbody')
		items = [] 
		for site in sites:
			item = ILGAitems()
			item['name'] = (site.select('//tr/td[2]/a/text()').extract()).encode('ascii','replace')
			item['legislative_number'] = (site.select('//tr/td/a/text()').extract()).encode(ascii','replace')  
			item ['chamber'] = (site.select('//tr/td[4]').extract()).encode(ascii','replace')  
			item ['last_action'] = (site.select('//tr/td[5]').extract()).encode(ascii','replace')   
			item ['last_action_date'] = (site.select('//tr/td[6]').extract()).encode(ascii','replace')   
			items.append(item)
		return items
