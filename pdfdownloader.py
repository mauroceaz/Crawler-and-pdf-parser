import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class pdf(scrapy.Spider):
    name = 'download'
    start_urls = ["http://www.anppom.com.br/congressos/index.php/29anppom/29CongrAnppom/schedConf/presentations"]

    def parse(self, response):
        for link in response.xpath('//div[@id="content"]/table/tbody/tr/td[2]/a'):
            loader = ItemLoader(item=SpiderItem(), selector=link)
            loader.add_value('file_urls', link)
            yield loader.load_item()
