from scrapy.spider import Spider
from scrapy import Selector
from scrapy.http import Request

from funda.items import FundaItem
from funda.utils import get_absolute_url


class FundaSpider(Spider):
    name = "funda_spider"
    allowed_domains = ["www.funda.nl"]
    start_urls = ["http://www.funda.nl/koop/verkocht/provincie-noord-brabant,provincie-zeeland,provincie-limburg/50000-600000/"]
    items = set([])
    count = 0

    def parse(self, response):
        return Request(self.start_urls[0], callback=self.parse_items)

    def parse_items(self, response):
        selector = Selector(response)
        items = selector.xpath('//*[@class="object-list"]/li/div[@class="specs"]')
        for item in items:
            funda_item = FundaItem()
            funda_item['street_name'] = item.xpath('h3/a/text()').extract()[0].strip()
            funda_item['post_code'] = item.xpath('ul/li/text()').extract()[0].strip()
            funda_item['price'] = item.xpath('span/span[@class="price"]/text()').extract()[0].strip()
            funda_item['date'] = item.xpath('span/span[@class="date"]/text()').extract()[0].strip()
            self.items.add(funda_item)
        next_page = selector.xpath('//*[@class="paging next"]/@href').extract()[0]
        if next_page and self.count < 10:
            self.count += 1
            return Request(get_absolute_url(next_page),
                           callback=self.parse_items)
        return self.items
