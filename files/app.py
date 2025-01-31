import requests
import logging
from flask import Flask, jsonify
from db import get_connection, init_db, insert_stock_price

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/api/v1/stock_prices', methods=['GET'])

def get_data():
    symbol = input('Enter a stock symbol: ')
    if not symbol:
        return jsonify({'error': 'Stock symbol is required'}), 400
    
    api_key = 'ML7626K7U6N2BGXZ'
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey='
        request = url + api_key
        response = requests.get(request)
        logger.debug(f'Response completed with status code {response.status_code}')
        data = response.json()
        
        if 'Weekly Time Series' in data:
            weekly_data = data['Weekly Time Series']
            connection = get_connection()
            cursor = connection.cursor()
            
            for date, values in weekly_data.items():
                price = values.get('4. close')
                insert_stock_price(cursor, symbol, price, date)
                logger.info(f'Inserted stock price for {symbol} on {date}')
                
            connection.commit()
            cursor.close()
            connection.close()
            logger.info('Transaction committed and connection closed. ')
            # return jsonify({'message': 'Data inserted successfully'}), 200
        else:
            logger.error('No weekly data found in the response')
        
        return jsonify(data)
    except Exception as e:
        logger.error(f'An error occurred: {e}')
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    init_db()
    from waitress import serve
    logger.info('Starting the server...')
    try:
        serve(app, host="0.0.0.0", port=8000)
    except InterruptedError:
        logger.info('Stopping the server...')