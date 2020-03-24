from flask import Flask, render_template
from flask_pymongo import PyMongo
import json
import requests
from datetime import datetime
import pytz

app = Flask(__name__,
            static_folder='./static')
app.config['MONGO_URI'] = 'mongodb://admin:123@mongo:27017/movie_cms'
mongo = PyMongo(app)


@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('home.html')

@app.route('/bar-chart')
def bar_chart():
    return render_template('barchart.html')
=======
    return render_template('index.html')
>>>>>>> add world data


@app.route('/fetch')
def fetch():
    params = {
        'spider_name': 'movie',
        'start_requests': True
    }
    response = requests.get('http://scrapy:9080/crawl.json', params)
    return response.text
