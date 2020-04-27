import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class anppom(scrapy.Spider):
    name = 'anppom'
    start_urls = ['http://www.anppom.com.br/congressos/index.php/28anppom/manaus2018/schedConf/presentations',
    'http://www.anppom.com.br/congressos/index.php/27anppom/cps2017/schedConf/presentations']

    def parse(self, response):
        for link in response.xpath('//a[contains(@class,"file")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse2)

    def parse2(self, response):
        dl = response.xpath('//a[4]/@href').extract()
        loader = ItemLoader(item=SpiderItem(), selector=dl)
        loader.add_value('file_urls', dl)
        yield loader.load_item()

class sbcm(scrapy.Spider):
    name = 'sbcm'
    start_urls = ["http://compmus.ime.usp.br/sbcm/"]

    def parse(self, response):
        for link in response.xpath('//following::li/a[3]/@href').extract():
            loader = ItemLoader(item=SpiderItem(), selector=link)
            urlabsoluta = response.urljoin(link)
            loader.add_value('file_urls', urlabsoluta)
            yield loader.load_item()
