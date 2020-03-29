# -*- coding: utf-8 -*-
import scrapy
from covid_ontario.items import CovidOntarioStatusItem, CovidOntarioCasesItem
from scrapy.utils.response import open_in_browser
import datetime


class OntarioSpider(scrapy.Spider):
    name = 'ontario'
    allowed_domains = ['www.ontario.ca']
    start_urls = [
        'https://www.ontario.ca/page/2019-novel-coronavirus'
    ]

    def parse(self, response):
        status_item = CovidOntarioStatusItem()
        status_dict = {
            'Negative': 'negative',
            'investigation': 'pending',
            'Confirmed': 'confirmed',
            'Resolved': 'resolved',
            'Total': 'total',
        }
        # status_table = response.css('.field-type-text-with-summary table')[0]
        # self.logger.warning('Table HTML %s', response)
        # open_in_browser(response)
        update_date = response.xpath(
            '//abbr[@title="Eastern Time"][1]/../text()')
        if update_date:
            date_strings = [x.strip() for x in update_date.get().split(': ')]
            date_string = date_strings[1].replace('.', '')
            date_timestamp = datetime.datetime.strptime(
                date_string, "%B %d, %Y at %I:%M %p").timestamp()
            status_item['date'] = date_timestamp
        for row in response.xpath('//table[1]//tr'):
            name = row.xpath('td[1]/descendant-or-self::*/text()').get()
            value = row.xpath('td[2]/descendant-or-self::*/text()').get()
            for label, key in status_dict.items():
                if name and value and label in name:
                    value = int(value.replace(',', ''))
                    self.logger.warning('Table Name %s', name)
                    self.logger.warning('Label %s', label)
                    status_item[key] = value
        yield status_item
