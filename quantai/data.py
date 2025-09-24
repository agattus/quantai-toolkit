"""
data.py
Handles fetching, cleaning, and preparing financial data
"""

import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period="6mo", interval="1d"):
    """
    Fetch historical stock data from Yahoo Finance
    """
    df = yf.download(ticker, period=period, interval=interval)
    df.reset_index(inplace=True)
    return df

def clean_data(df):
    """
    Simple cleaning: fill missing values
    """
    df = df.fillna(method="ffill")
    return df

if __name__ == "__main__":
    df = fetch_stock_data("AAPL")
    df = clean_data(df)
    print(df.head())
