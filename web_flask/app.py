from flask import Flask
from flask_pymongo import PyMongo
import json
import requests
from urllib.parse import quote_plus

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://admin:123@mongo:27017/movies_cms"
mongo = PyMongo(app)


@app.route('/')
def hello():
    params = {
        'spider_name': 'movie',
        'start_requests': True
    }
    response = requests.get('http://scrapy:9080/crawl.json', params)
    data = json.loads(response.text)
    movies = mongo.db.movies.find({"year": "2013"})
    result = '\n'.join(
        '<p><b>{}</b> - {}</p>'.format(item['title'], item['url']) for item in movies)
    return result
