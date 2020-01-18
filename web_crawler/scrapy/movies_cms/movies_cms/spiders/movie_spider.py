import scrapy

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ["movie.thepan.cn"]
    start_urls = [
        'https://movie.thepan.cn'
    ]