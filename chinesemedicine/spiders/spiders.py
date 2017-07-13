# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from chinesemedicine.items import ChinesemedicineItem
from scrapy.contrib.linkextractors import LinkExtractor
add =0
class ChineseMedicineSpider(CrawlSpider):
    name ="chineseMedicine"
    allowed_domains = ["www.tcminformatics.org"]
    start_urls = ['http://www.tcminformatics.org/wiki/index.php/baike/']
    rules = (
        Rule(LinkExtractor(allow=('search?/*',)), callback='parse_item', follow=True),
    )
    def parse_item(self,response):
        global add
        add += 1
        print add
        item = ChinesemedicineItem()
        medicineName = response.xpath('//div[@class="container"]/h1/font/text()').extract()
        item['medicineName'] = medicineName
        overView = response.xpath('//div[@id="use"]/div[@class="panel-body"]')
        overView= overView.xpath('string(.)').extract()
        #overView = response.xpath('//div[@class="panel-body"]/p/strong/text()|//div[@class="panel-body"]/p/text()').extract()
        item['overView'] = overView

        yield item