from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo
import json
import requests
from urllib.parse import quote_plus
from datetime import datetime
import pytz

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://admin:123@mongo:27017/movies_cms"
mongo = PyMongo(app)


@app.route('/')
def index():
    movies = mongo.db.movies.find()
    return render_template("index.html", movies=movies)

@app.route('/year/<year>')
def show_movie_by_year(year):
    movies = mongo.db.movies.find({"year": year})
    return render_template("index.html", movies=movies)

@app.route('/admin')
def admin():
    return render_template("dashboard.html")

@app.route('/fetch')
def fetch():
    params = {
        'spider_name': 'movie',
        'start_requests': True
    }
    response = requests.get('http://scrapy:9080/crawl.json', params)
    data = json.loads(response.text)
    movies = mongo.db.movies.find()
    result = '\n'.join(
        '<p><b>{}</b> - {}</p>'.format(item['title'], item['url']) for item in movies)
    return result


@app.route('/time')
def chart():
    legend = 'Crawling Movie Count'
    labels = []
    values = []
    for time in mongo.db.movies.distinct('time'):
        labels.append(datetime.fromtimestamp(int(time), pytz.timezone(
            'America/Toronto')))
        values.append(mongo.db.movies.find({"time": time}).count())
    return render_template('time_chart.html', values=values, labels=labels, legend=legend)


@app.route('/')
def hello():
    return 'This is a Flask CMS'
