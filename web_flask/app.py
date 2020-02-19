from flask import Flask, render_template
from flask_pymongo import PyMongo
import json
import requests
from urllib.parse import quote_plus

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

@app.route('/fetch')
def fetch():
    params = {
        'spider_name': 'movie',
        'start_requests': True
    }
    response = requests.get('http://scrapy:9080/crawl.json', params)
    data = json.loads(response.text)
    return render_template("index.html", message='Fetched New Data!')
