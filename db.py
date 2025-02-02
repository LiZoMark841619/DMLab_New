import pyodbc
import logging
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s, - %(message)s')
logger = logging.getLogger(__name__)

def get_connection():
    logger.info('Connecting to the database...')  # Debugging statement
    try:
        server = os.getenv("DATABASE_SERVER", "sql_server")
        database = os.getenv("DATABASE_NAME", "master")
        uid = os.getenv("UID", "sa")
        pwd = os.getenv("PWD", "DMLab_New123")
        conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={uid};'
            f'PWD={pwd};'
            'Connection Timeout=30;'
        )
        logger.info('Connected to the database')  # Debugging statement
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
            date_of_trade DATE,
            stock_symbol NVARCHAR(MAX),
            open_price FLOAT,
            close_price FLOAT
        )
    '''
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    logger.info("Table 'stock_prices' created successfully")  # Debugging statement

def record_exists(cursor, date_of_trade, stock_symbol):
    query = "SELECT COUNT(*) FROM stock_prices WHERE date_of_trade = ? AND stock_symbol = ?"
    cursor.execute(query, (date_of_trade, stock_symbol))
    count = cursor.fetchone()[0]
    return count > 0

def insert_stock_price(cursor, date_of_trade, stock_symbol, open_price, close_price):
    if not record_exists(cursor, date_of_trade, stock_symbol):
        query = "INSERT INTO stock_prices (date_of_trade, stock_symbol, open_price, close_price) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (date_of_trade, stock_symbol, open_price, close_price))
        logger.info(f'Inserted stock price for {stock_symbol}.') # Debugging statement
    else:
        logger.info(f'Record for {stock_symbol} on {date_of_trade} already exists.')