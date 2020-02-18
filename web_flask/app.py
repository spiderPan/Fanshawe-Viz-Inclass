from flask import Flask
import json
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    params = {
        'spider_name': 'fanshaweSpider',
        'start_requests': True
    }
    response = requests.get('http://scrapy:9080/crawl.json', params)
    data = json.loads(response.text)
    result = '\n'.join('<p><b>{}</b> - {}</p>'.format(item['code'], item['coordinator'])
                       for item in data['items'])
    return result
