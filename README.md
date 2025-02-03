# DMLab_New

## Overview
DMLab_New is a Flask-based web application that fetches and stores stock prices from the Alpha Vantage API and provides endpoints to retrieve and plot the data.

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd DMLab_New
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your Alpha Vantage API key:
    ```env
    API_KEY=your_alpha_vantage_api_key
    ```

5. Initialize the database:
    ```sh
    python -c "from db import init_db; init_db()"
    ```

6. Run the application:
    ```sh
    python app.py
    ```

## API Endpoints

### Fetch Stock Prices
- **URL:** `/api/v1/stock_prices`
- **Method:** `GET`
- **Query Parameters:**
  - `symbol` (required): The stock symbol to fetch data for.
- **Response:**
  - JSON object containing the stock prices or an error message.

### Plot Stock Prices
- **URL:** `/api/v1/stock_prices/plot`
- **Method:** `GET`
- **Query Parameters:**
  - `symbol` (required): The stock symbol to plot data for.
- **Response:**
  - HTML content of the plot or an error message.

## Logging
The application uses Python's built-in logging module to log debug and error messages. Logs are printed to the console.

## License
This project is licensed under the MIT License.