import scrapy

from movies_cms.items import MoviesCmsItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ["movie.thepan.cn"]
    start_urls = [
        'https://movie.thepan.cn'
    ]

    def parse(self, response):
        movies = scrapy.Selector(response).css('.movie-item')

        for movie in movies:
            movie_item = MoviesCmsItem()
            movie_item['title'] = movie.css('h2::text').get().strip()
            movie_item['url'] = movie.css('a').attrib['href']
            yield movie_item
