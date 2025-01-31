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
            column2 FLOAT,
            column3 DATE
        )
    '''
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    logging.debug("Table 'stock_prices' created successfully")  # Debugging statement
    

def insert_stock_price(cursor, stock_symbol, price, date):
    query = "INSERT INTO stock_prices (column1, column2, column3) VALUES (?, ?, ?)"
    cursor.execute(query, (stock_symbol, price, date))
    logger.info(f'Inserted stock price for {stock_symbol}.')
