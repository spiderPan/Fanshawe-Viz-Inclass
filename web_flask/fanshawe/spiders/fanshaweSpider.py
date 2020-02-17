# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from fanshawe.items import FanshaweItem

class FanshawespiderSpider(CrawlSpider):
    name = 'fanshaweSpider'
    allowed_domains = ['fanshawec.ca']
    start_urls = ['https://www.fanshawec.ca/programs-and-courses']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.fanshawec.ca/programs/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        fanshaweItem = FanshaweItem()
        fanshaweItem['name'] = response.css('#page-title::text').get().strip()
        fanshaweItem['code'] = response.css('.views-field-field-program-code .field-content::text').get().strip()
        fanshaweItem['school'] = response.css('.field-name-field-academic-school a::text').get().strip()
        fanshaweItem['duration'] = response.css('.views-field-field-duration-next .field-content::text').get().strip()
        fanshaweItem['coordinator'] = response.css('.field-name-field-program-coordinator p::text').get().strip()

        return fanshaweItem
