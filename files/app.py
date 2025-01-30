import requests
import logging
from flask import Flask, jsonify

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/api/v1/ibm', methods=['GET'])

def get_data():
    symbol = input('Enter a stock symbol: ')
    api_key = 'ML7626K7U6N2BGXZ'
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey='
        request = url + api_key
        response = requests.get(request)
        logger.debug(f'Response completed with status code {response.status_code}')
        return jsonify(response.json())
    except Exception as e:
        return logger.error(f'An error occurred: {e}')

if __name__ == '__main__':
    from waitress import serve
    logger.info('Starting the server...')
    try:
        serve(app, host="0.0.0.0", port=8000)
    except InterruptedError:
        logger.info('Stopping the server...')
