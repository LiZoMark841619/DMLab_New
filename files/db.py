import pyodbc
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s, - %(message)s')
logger = logging.getLogger(__name__)

def get_connection():
    logging.debug('Connecting to the database...')  # Debugging statement
    try:
        conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost\SQLEXPRESS;'
        'DATABASE=master;'
        'Trusted_Connection=yes;')
        logger.debug('Connected to the database')  # Debugging statement
        return conn
    except Exception as e:
        logger.error(f'Error connecting to the database: {e}')  # Debugging statement
        raise

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='stock_prices' AND xtype='U')
        CREATE TABLE stock_prices (
            id INT PRIMARY KEY IDENTITY(1,1),
            column1 NVARCHAR(MAX),
            column2 NVARCHAR(MAX),
            column3 NVARCHAR(MAX),
            column4 NVARCHAR(MAX)
        )
    '''
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    logging.debug("Table 'stock_prices' created successfully")  # Debugging statement
    
#from here the code is not working above this line it is working fine

def insert_stock_price(cursor, stock_symbol, price):
    query = f"INSERT INTO {TABLE_NAME} (symbol, price) VALUES (?, ?)"
    cursor.execute(query, (stock_symbol, price))
    logging.info(f'Inserted stock price for {stock_symbol}.')

def main():
    logging.debug('Starting main function.')
    try:
        connection = get_connection()
        cursor = connection.cursor()
        insert_stock_price(cursor, 'AAPL', 150.00)
        connection.commit()
        logging.info('Transaction committed.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    finally:
        connection.close()
        logging.debug('Connection closed.')

if __name__ == '__main__':
    main()