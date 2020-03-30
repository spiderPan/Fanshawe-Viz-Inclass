# -*- coding: utf-8 -*-
import scrapy
from covid_ontario.items import CovidOntarioStatusItem
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
            'Number of cases': 'confirmed',
            'Resolved': 'resolved',
            'Deceased': 'deceased',
            'Investigation': 'pending',
            'Total': 'total',
        }
        # status_table = response.css('.field-type-text-with-summary table')[0]
        # self.logger.warning('Table HTML %s', response)
        open_in_browser(response)
        date_timestamp = datetime.datetime.now().strftime("%B %d, %Y")
        status_item['date'] = date_timestamp
        for row in response.xpath('//table[1]/tbody/tr'):
            name = row.xpath(
                'td[1]/descendant-or-self::*/text()').get().strip()
            value = row.xpath(
                'td[2]/descendant-or-self::*/text()').get().strip()
            for label, key in status_dict.items():
                if name and value and label in name:
                    value = int(value.replace(',', ''))
                    # self.logger.warning('Table Name %s', name)
                    # self.logger.warning('Label %s', label)
                    # self.logger.warning('Value %s', value)
                    status_item[key] = value
        yield status_item
