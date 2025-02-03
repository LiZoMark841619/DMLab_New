import os
import requests
import logging
import plotly.graph_objects as go
from dotenv import load_dotenv
from waitress import serve
from flask import Flask, jsonify, request
from db import get_connection, init_db, insert_stock_price

load_dotenv()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/api/v1/stock_prices', methods=['GET'])
def fetch_data():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Stock symbol is required'}), 400
    
    apikey = os.getenv('API_KEY')
    try:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey='
        endpoint = url + apikey
        response = requests.get(endpoint)
        logger.debug(f'Response completed with status code {response.status_code}') # Debugging statement
        data = response.json()
        
        if 'Weekly Time Series' in data:
            weekly_data = data['Weekly Time Series']
            connection = get_connection()
            cursor = connection.cursor()

            for date, values in weekly_data.items():
                open_price = values.get('1. open')
                close_price = values.get('4. close')
                insert_stock_price(cursor, date, symbol, open_price, close_price)
                logger.info(f'Inserted stock price for {symbol} on {date}')

            connection.commit()
            cursor.close()
            connection.close()
            logger.info('Transaction committed and connection closed. ')

        logger.error('No weekly data found in the response')
        return jsonify(data)

    except Exception as e:
        logger.error(f'An error occurred: {e}')
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/api/v1/stock_prices/plot', methods=['GET'])
def make_a_plot():
    symbol = request.args.get('symbol')
    if not symbol:
        logger.error('Stock symbol is required')
        return jsonify({'error': 'Stock symbol is required'}), 400
    
    connection = get_connection()
    cursor = connection.cursor()
    query = 'SELECT date_of_trade, open_price, close_price FROM stock_prices WHERE stock_symbol = ?'
    rows = cursor.execute(query, (symbol,)).fetchall()

    if not rows:
        logger.error(f'No data found for {symbol}')
        return jsonify({'error': f'No data found for {symbol}'}), 404

    dates = [r[0] for r in rows]
    open_prices = [r[1] for r in rows]
    close_prices = [r[2] for r in rows]
    
    logger.debug(f'Dates: {dates}, Open prices: {open_prices}, Close prices: {close_prices}')
    
    fig = go.Figure(data=[go.Scatter(x=dates, y=open_prices, mode='lines', name='Open Prices')])
    fig.add_trace(go.Scatter(x=dates, y=close_prices, mode='lines', name='Close Prices'))
    fig.update_layout(title=f'{symbol} stock price', xaxis_title='Date', yaxis_title='Price')
    return fig.to_html(full_html=False)

if __name__ == '__main__':
    init_db()
    logger.info('Starting the server...') # Debugging statement
    try:
        serve(app, host="0.0.0.0", port=5000)
    except InterruptedError:
        logger.info('Stopping the server...') # Debugging statement