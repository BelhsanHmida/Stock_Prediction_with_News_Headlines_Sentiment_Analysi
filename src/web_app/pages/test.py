import yfinance as yf
import pandas as pd
import streamlit as st

# Function to fetch stock data
def fetch_stock_data(symbol):
    stock_data = yf.download(symbol, start='2022-01-01', end='2022-04-01')
    return stock_data

# Function to calculate percentage change and determine up/down status
def calculate_change(stock_data):
    if len(stock_data) < 2:
        return None, None, "Insufficient data"
    latest_price = stock_data['Close'].iloc[-1]
    previous_price = stock_data['Close'].iloc[-2]
    percent_change = ((latest_price - previous_price) / previous_price) * 100
    status = "Up" if percent_change > 0 else "Down"
    return latest_price, percent_change, status

# Fetch data for NVIDIA, Meta Platforms, Google, Microsoft, Tesla, and Twitter
symbols = ['NVDA', 'FB', 'GOOGL', 'MSFT', 'TSLA', 'TWTR']
data = []
for symbol in symbols:
    stock_data = fetch_stock_data(symbol)
    price, percent_change, status = calculate_change(stock_data)
    if price is not None and percent_change is not None:
        data.append({'Stock': symbol, 'Price': price, 'Change (%)': percent_change, 'Status': status})

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame in Streamlit app
st.write(df)
