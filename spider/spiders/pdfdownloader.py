import scrapy
from scrapy.loader import ItemLoader
from spider.items import SpiderItem

class anppom(scrapy.Spider):
    name = 'anppom'
    start_urls = ['http://www.anppom.com.br/congressos/index.php/29anppom/29CongrAnppom/schedConf/presentations',
    'http://www.anppom.com.br/congressos/index.php/28anppom/manaus2018/schedConf/presentations',
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

class opus1(scrapy.Spider):
    name = 'opus1'
    start_urls = ['http://www.anppom.com.br/revista/index.php/opus/issue/view/49/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/48/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/47/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/46/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/45/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/43/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/42/showToc']

    def parse(self, response):
        for link in response.xpath('//a[contains(@class,"file")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse2)

    def parse2(self, response):
        dl = response.xpath('//a[contains(@class,"action pdf")]/@href').extract()
        loader = ItemLoader(item=SpiderItem(), selector=dl)
        loader.add_value('file_urls', dl)
        yield loader.load_item()

class opus2(scrapy.Spider):
    name = 'opus2'
    start_urls = ['http://www.anppom.com.br/revista/index.php/opus/issue/view/39/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/38/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/37/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/36/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/35/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/21.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/21,1/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/20.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/20.1/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/19.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/19.1/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/18.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/18.1/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/17.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/17.1/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/16.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/16.1/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/15.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/15.1/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/14.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/14.1/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/13.2/showToc',
    'http://www.anppom.com.br/revista/index.php/opus/issue/view/13.1/showToc']

    def parse(self, response):
        for link in response.xpath('//a[contains(@class,"file")]/@href').extract():
            yield scrapy.Request(link,meta={'dont_redirect': True}, callback=self.parse2)

    def parse2(self, response):
        dl = response.xpath('//div/a[contains(@class,"action")]/@href').extract()
        loader = ItemLoader(item=SpiderItem(), selector=dl)
        loader.add_value('file_urls', dl)
        yield loader.load_item()
