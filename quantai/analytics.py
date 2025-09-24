"""
analytics.py
Compute technical indicators and other analytics
"""

import pandas as pd

def moving_average(df, column="Close", window=20):
    """
    Compute simple moving average (SMA)
    """
    df[f"SMA_{window}"] = df[column].rolling(window=window).mean()
    return df

def exponential_moving_average(df, column="Close", window=20):
    """
    Compute exponential moving average (EMA)
    """
    df[f"EMA_{window}"] = df[column].ewm(span=window, adjust=False).mean()
    return df

def relative_strength_index(df, column="Close", window=14):
    """
    Compute RSI indicator
    """
    delta = df[column].diff()
    gain = delta.clip(lower=0)
    loss = -1*delta.clip(upper=0)
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df

if __name__ == "__main__":
    import quantai.data as data
    df = data.fetch_stock_data("AAPL")
    df = moving_average(df)
    df = exponential_moving_average(df)
    df = relative_strength_index(df)
    print(df.tail())
