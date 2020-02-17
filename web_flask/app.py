from flask import Flask

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from fanshawe.spiders.fanshaweSpider import FanshawespiderSpider

app = Flask(__name__)

@app.route('/')

def hello():
    process = CrawlerProcess(get_project_settings())

    # process.crawl(FanshawespiderSpider)
    # process.start()  # the script will block here until the crawling is finished
    return 'Start Spider.\n'
