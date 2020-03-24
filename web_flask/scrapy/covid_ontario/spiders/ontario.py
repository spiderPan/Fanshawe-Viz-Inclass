# -*- coding: utf-8 -*-
import scrapy
from covid_ontario.items import CovidOntarioStatusItem, CovidOntarioCasesItem
from scrapy.utils.response import open_in_browser


class OntarioSpider(scrapy.Spider):
    name = 'ontario'
    allowed_domains = ['https://www.ontario.ca']
    start_urls = [
        'https://www.ontario.ca/page/2019-novel-coronavirus'
    ]

    def parse(self, response):
        status_item = CovidOntarioStatusItem()
        status_dict = {
            'negative': 'Negative',
            'pending': 'investigation',
            'confirmed': 'Confirmed',
            'resolved': 'Resolved',
            'total': 'Total',
        }
        status_table = response.css('.field-type-text-with-summary table')[0]
        # self.logger.warning('Table HTML %s', status_table.get())
        #Debug in Browser
        # open_in_browser(response)
        date_strings = [x.strip() for x in response.css(
            '#last-modified::text').get().split(':')]
        status_item['date'] = date_strings[1]
        for row in status_table.css('tr'):
            for key, name in status_dict.items():
                row_name = row.css('td:first-child::text').get()
                if row_name and name in row_name:
                    value = int(row.css('td:last-child::text').get())
                    status_item[key] = value
        yield status_item

        case_table = response.css('.field-type-text-with-summary table')[1]
        for row in case_table.css('tbody tr'):
            row_data = row.css('td::text').getall()
            case_item = CovidOntarioCasesItem()
            case_item['case_number'] = row_data[0]
            case_item['age_and_gender'] = row_data[1]
            case_item['public_health_unit'] = row_data[2]
            case_item['hospital'] = row_data[3]
            case_item['transmission'] = row_data[4]
            case_item['status'] = row_data[5]
            case_item['date'] = date_strings[1]
            yield case_item
