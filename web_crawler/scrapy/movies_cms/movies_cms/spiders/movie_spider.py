import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from movies_cms.items import MoviesCmsItem


class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ["movie.thepan.cn"]
    start_urls = [
        'https://movie.thepan.cn'
    ]

    rules = (
        Rule(LinkExtractor(allow=('details\.php',)), callback='parse_item'),
    )

    def parse_item(self, response):
        movie_item = MoviesCmsItem()
        movie_item['title'] = response.css('h2::text')[1].get().strip()
        movie_item['url'] = response.url
        movie_item['image'] = response.css('img').attrib['src']
        movie_item['year'] = response.css('p::text')[0].get().strip()
        yield movie_item
