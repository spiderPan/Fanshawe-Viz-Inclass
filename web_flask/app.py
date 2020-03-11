from flask import Flask
from flask_pymongo import PyMongo
import json
import requests
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://admin:123@mongo:27017/movie_cms'
mongo = PyMongo(app)


@app.route('/')
def index():
    return '<h1>This is a Flask CMS</h1>'


@app.route('/fetch')
def fetch():
    params = {
        'spider_name': 'movie',
        'start_requests': True
    }
    response = requests.get('http://scrapy:9080/crawl.json', params)
    return response.text
