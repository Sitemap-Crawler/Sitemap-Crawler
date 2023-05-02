import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def submit_url():
    content_length = int(request.headers['Content-Length'])
    post_data = request.get_data().decode('utf-8')
    parsed_data = json.loads(post_data)
    if 'url' in parsed_data:
        url = parsed_data['url']
        print("Submitted URL: {}".format(url))
        response_data = {'status': 'success', 'message': 'URL received successfully'}
        return make_response(jsonify(response_data), 200)
    else:
        response_data = {'status': 'error', 'message': 'URL not found in payload'}
        return make_response(jsonify(response_data), 400)

@app.route('/urlCheck', methods=['POST'])
def crawl_sitemap():
    content_length = int(request.headers['Content-Length'])
    post_data = request.get_data().decode('utf-8')
    parsed_data = json.loads(post_data)
    if 'url' in parsed_data:
        url = parsed_data['url']
        print("Crawling sitemap: {}".format(url))
        # Send a GET request to the sitemap URL
        response = requests.get(url)
        # Parse the sitemap XML using BeautifulSoup with lxml parser
        soup = BeautifulSoup(response.text, 'lxml')
        # Find all the URLs in the sitemap
        urls = [loc.text for loc in soup.find_all('loc')]
        # Crawl each URL
        for url in urls:
            requests.get(url)
        response_data = {'status': 'success', 'message': 'Sitemap crawled successfully'}
        return make_response(jsonify(response_data), 200)
    else:
        response_data = {'status': 'error', 'message': 'Sitemap URL not found in payload'}
        return make_response(jsonify(response_data), 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
