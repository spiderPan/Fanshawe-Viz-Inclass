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


@app.route('/')
def index():
    status = mongo.db.status
    status_data = []
    for s in status.find():
        date_object = datetime.fromtimestamp(s['date'])
        status_data.append({'date': date_object.isoformat(),
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
    return response.text
