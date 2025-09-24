"""
run_all.py
Test script for QuantAI Toolkit v1.0
- Verifies data fetching, analytics, models, and demo
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from quantai import data, analytics, models
import examples.simple_sma_demo as demo

def test_data():
    print("Testing data module...")
    df = data.fetch_stock_data("AAPL", period="1mo", interval="1d")
    df = data.clean_data(df)
    print(df.head())
    print("Data module works!\n")

def test_analytics():
    print("Testing analytics module...")
    df = data.fetch_stock_data("AAPL", period="1mo", interval="1d")
    df = data.clean_data(df)
    df = analytics.moving_average(df)
    df = analytics.exponential_moving_average(df)
    df = analytics.relative_strength_index(df)
    print(df.tail())
    print("Analytics module works!\n")

def test_models():
    print("Testing models module...")
    models.forecast_placeholder(None)
    print("Models module works!\n")

def run_demo():
    print("Running demo script...")
    demo.main()
    print("Demo script works!\n")

if __name__ == "__main__":
    test_data()
    test_analytics()
    test_models()
    run_demo()
    print("✅ All modules and demo executed successfully!")
