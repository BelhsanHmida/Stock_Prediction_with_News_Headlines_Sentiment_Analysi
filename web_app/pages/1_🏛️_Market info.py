import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd 

st.set_page_config(page_title="Market Info", page_icon="🏛️", layout="wide")

st.sidebar.title("Stock Analysis")
st.title('🏛️ Market Info' )
# Input field for entering stock name
stock_name = st.sidebar.text_input("Enter Stock Name", value="AMZN", max_chars=10)

# Selectbox for choosing the time frame
time_frame = st.sidebar.selectbox("Select Time Frame", ["1d", "1wk", "1mo", "3mo"], index=2)
st.header('Trending Stocks: ')
start=st.sidebar.date_input('Start Date', value=pd.to_datetime('2020-01-01'))
end=st.sidebar.date_input('End Date', value=pd.to_datetime('2022-01-01'))

def fetch_stock_data(symbol):
    stock_data = yf.download(symbol, start=start, end=end)
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
symbols = ['NVDA', 'FB', 'GOOG', 'MSFT', 'TSLA', 'TWTR']
data = []

red_color = '#ff0000'  # Red color
green_color = '#00ff00'  # Green color

for symbol in symbols:
    stock_data = fetch_stock_data(symbol)
    price, percent_change, status = calculate_change(stock_data)
    if price is not None and percent_change is not None:
        data.append({'Stock': symbol, 'Price': price, 'Change (%)': percent_change, 'Status': status})

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame in Streamlit app
st.write(df)

# Fetch financial data using yfinance
try:
        
    stock_data = yf.download(stock_name, period=time_frame)

    # Plot closing price
    st.subheader("Closing Price")
    fig_close = go.Figure()
    fig_close.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Closing Price'))
    fig_close.update_layout(title=f"Closing Price for {stock_name}", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig_close)

    # Plot volume
    st.subheader("Volume")
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Bar(x=stock_data.index, y=stock_data['Volume'], name='Volume', marker_color='rgb(26, 118, 255)'))
    fig_volume.update_layout(title=f"Volume for {stock_name}", xaxis_title="Date", yaxis_title="Volume")
    st.plotly_chart(fig_volume)
    
except Exception as e:
    st.error(f"Error: {e}")
