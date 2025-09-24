"""
simple_sma_demo.py
Demo script for QuantAI Toolkit:
- Fetch stock data
- Compute SMA, EMA, RSI
- Plot results
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib.pyplot as plt
from quantai import data, analytics

def main():
    # 1️⃣ Fetch and clean data
    df = data.fetch_stock_data("AAPL", period="6mo", interval="1d")
    df = data.clean_data(df)

    # 2️⃣ Compute indicators
    df = analytics.moving_average(df, window=20)
    df = analytics.exponential_moving_average(df, window=20)
    df = analytics.relative_strength_index(df)

    # 3️⃣ Plot closing price and indicators
    plt.figure(figsize=(14,7))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['SMA_20'], label='SMA 20', color='orange')
    plt.plot(df['Date'], df['EMA_20'], label='EMA 20', color='green')
    plt.title("AAPL Stock Price with SMA & EMA")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 4️⃣ Plot RSI separately
    plt.figure(figsize=(14,4))
    plt.plot(df['Date'], df['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title("Relative Strength Index (RSI)")
    plt.xlabel("Date")
    plt.ylabel("RSI")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
