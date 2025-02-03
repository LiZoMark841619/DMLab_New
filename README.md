# DMLab Project

## Overview
DMLab is a Flask-based web application for fetching and visualizing stock prices.

## Features
- Fetch stock prices from an external API
- Store data in SQL Server
- Visualize data using Plotly

## Setup Options

### Option 1: Clone Repository and Run Locally

1. **Clone the repository**
    ```bash
    git clone https://github.com/LiZoMark841619/DMLab_New.git
    cd DMLab_New
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv_new
    source venv_new/bin/activate  # On Windows use `source venv_new\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**
    ```bash
    cp .env.example .env
    # Edit .env file to add your API_KEY, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, and DB_NAME
    ```

5. **Run the application**
    ```bash
    flask run
    ```

### Option 2: Using Docker

1. **Clone the repository**
    ```bash
    git clone https://github.com/LiZoMark841619/DMLab_New.git
    cd DMLab_New
    ```

2. **Set up environment variables**
    ```bash
    cp .env.example .env
    # Edit .env file to add your API_KEY, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, and DB_NAME
    ```

3. **Build and run the Docker containers**
    ```bash
    docker-compose up -d --build
    ```

4. **Access the application**
    - Open your browser and go to `http://localhost:5000`

## API Endpoints
- `/api/v1/stock_prices?symbol=AAPL` - Fetch stock prices for a given symbol
- `/api/v1/stock_prices/plot?symbol=AAPL` - Fetch and plot stock prices for a given symbol

## Logging
The application uses Python's built-in logging module to log debug and error messages. Logs are printed to the console.

## Contributing
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request