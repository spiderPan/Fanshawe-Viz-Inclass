from flask import Flask
import json
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    params = {
        'spider_name': 'movie',
        'start_requests': True
    }
    response = requests.get('http://scrapy:9080/crawl.json', params)
    data = json.loads(response.text)
    result = '\n'.join('<p><b>{}</b> - {}</p>'.format(item['title'], item['url'])
                       for item in data['items'])
    return result
