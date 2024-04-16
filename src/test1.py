import yfinance as yf
import streamlit as st
import mplfinance as mpf
import matplotlib.pyplot as plt
import time
from streamlit_option_menu import option_menu
# Function to fetch historical stock data for Amazon (AMZN)
def fetch_stock_data():
    stock_data = yf.download('AMZN', start='2021-01-01', end='2022-01-01')
    stock_data.reset_index(inplace=True)
    stock_data.set_index('Date', inplace=True)
    return stock_data

# Function to plot the candlestick chart
def plot_candlestick_chart(data):
    mpl_style = mpf.make_mpf_style(base_mpl_style="seaborn-darkgrid", rc={"font.size": 10})
    kwargs = dict(type='candle', volume=True, title='Candlestick Chart for AMZN Stock (2021-2022)', style=mpl_style)
    fig, ax = plt.subplots()
    mpf.plot(data, ax=ax, volume=ax, **kwargs)
    return fig

# Define page content for Page 1
def page_home():
 
    st.write(
    """# 📈 **Stockastic**
### **Predicting Stocks with ML**

**Stockastic is an ML-powered stock price prediction app built with Python and Streamlit. It utilizes machine learning models to forecast stock prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

Stockastic is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Plotly** - To create interactive financial charts

The app workflow is:

1. User selects a stock ticker
2. Historical data is fetched with YFinance
3. ARIMA model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

## 🎯 **Key Features**

- **Real-time data** - Fetch latest prices and fundamentals 
- **Financial charts** - Interactive historical and forecast charts
- **ARIMA forecasting** - Make statistically robust predictions
- **Backtesting** - Evaluate model performance
- **Responsive design** - Works on all devices

## 🚀 **Getting Started**

### **Local Installation**

1. Clone the repo

```bash
git clone https://github.com/user/stockastic.git
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. Change directory
```bash
cd streamlit_app
```

4. Run the app

```bash
streamlit run 00_😎_Main.py
```

The app will be live at ```http://localhost:8501```

## 📈 **Future Roadmap**

Some potential features for future releases:

- **More advanced forecasting models like LSTM**
- **Quantitative trading strategies**
- **Portfolio optimization and tracking**
- **Additional fundamental data**
- **User account system**

## **⚖️ Disclaimer**
**This is not financial advice! Use forecast data to inform your own investment research. No guarantee of trading performance.**
"""
)

# Define page content for Page 2
def page_candlestick_chart():
    st.title('Candlestick Chart')
    st.write('This is the candlestick chart for AMZN stock.')
    # Fetch and plot stock data
    stock_data = fetch_stock_data()
    fig = plot_candlestick_chart(stock_data)
    # Display the chart in Streamlit
    st.pyplot(fig)

# Define page content for Page 3 (About page)
def page_about():
    st.title("About")
    st.write("This is the About page.")

# Function for the "Market Info" page
def page_market_info():
    st.title("Market Info")
    st.write("This is the Market Info page.")
    # Add a dropdown in the sidebar for inputting a number
    number = st.sidebar.number_input("Enter a number", min_value=1, max_value=10, value=5)

# Function for the "Market Predict" page
def page_market_predict():
    st.title("Market Predict")
    st.write("This is the Market Predict page.")

# Function to handle page navigation
def main():
    
    with st.sidebar:
        page=option_menu(
            menu_title=None,
            options=['🏛️ About', '📰 Market Info', '📈 Market Predict'])
    # Render the selected page content
    if page == "Home":
        page_home()
    elif page == "Market Info":
        page_market_info()
    elif page == "Market Predict":
        page_market_predict()

if __name__ == "__main__":
    main()