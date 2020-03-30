from flask import Flask, render_template
from flask_pymongo import PyMongo
import json
import requests
from datetime import datetime
import pytz

app = Flask(__name__,
            static_folder='./static')
app.config['MONGO_URI'] = 'mongodb://admin:123@mongo:27017/covid_ontario'
mongo = PyMongo(app)


@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = datetime.fromtimestamp(date)
    native = date.replace(tzinfo=None)
    format = '%B %d, %Y at %I:%M %p'
    return native.strftime(format)


@app.route('/')
def index():
    status = mongo.db.status
    status_data = []
    for s in status.find():
        status_data.append({'date': s['date'],
                            'negative': s['negative'],
                            'pending': s['pending'],
                            'confirmed': s['confirmed'],
                            'resolved': s['resolved'],
                            'total': s['total']
                            })
    return render_template('home.html', ontario_data=status_data)


@app.route('/bar-chart')
def bar_chart():
    return render_template('barchart.html')


@app.route('/fetch')
def fetch():
    params = {
        'spider_name': 'ontario',
        'start_requests': True
    }
    response = requests.get('http://scrapy:9080/crawl.json', params)
    fetch_result = json.loads(response.text)
    return render_template('fetch.html', content=fetch_result)
