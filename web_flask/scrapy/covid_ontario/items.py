# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidOntarioStatusItem(scrapy.Item):
    negative = scrapy.Field()
    pending = scrapy.Field()
    confirmed = scrapy.Field()
    resolved = scrapy.Field()
    total = scrapy.Field()
    date = scrapy.Field()
    pass

# Ontario stopped update case info

# class CovidOntarioCasesItem(scrapy.Item):
#     case_number = scrapy.Field()
#     age_and_gender = scrapy.Field()
#     public_health_unit = scrapy.Field()
#     hospital = scrapy.Field()
#     transmission = scrapy.Field()
#     status = scrapy.Field()
#     date = scrapy.Field()
#     pass
