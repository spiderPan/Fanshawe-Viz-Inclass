# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidOntarioItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    deceased = scrapy.Field()
    confirmed = scrapy.Field()
    pending = scrapy.Field()
    resolved = scrapy.Field()
    total = scrapy.Field()
    date = scrapy.Field()
    pass
