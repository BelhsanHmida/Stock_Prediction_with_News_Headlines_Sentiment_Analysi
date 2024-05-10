import streamlit as st 
 
st.set_page_config(page_title="SentimentTrader", page_icon="😎" , layout="wide")

st.title("📈 SentimentTrader")
st.header("Predicting Stocks with Sentiment Analysis")
st.write(
    "SentimentTrader is an AI-powered stock price prediction app built with Python and Streamlit. "
    "It utilizes deep learning models to forecast stock prices and help investors make data-driven decisions."
)

# Section: How It's Built
st.header("🏗️ How It's Built")
st.write(
    "SentimentTrader is built with these core frameworks and modules:"
)

# List the frameworks and modules used
st.markdown(
    """
    - **Streamlit**: Framework to create the web app's user interface and interactivity.
    - **YFinance**: Library to fetch financial data from the Yahoo Finance API.
    - **Plotly**: Data visualization library used to create interactive financial charts.
    - **Pandas**: Library for data manipulation and analysis.
    - **NLTK and TextBlob**: Libraries for natural language processing and sentiment analysis.
    - **Prophet**: Time series forecasting tool developed by Facebook for stock price prediction.
    - **Transformers**: Library providing pre-trained deep learning models; used for advanced sentiment analysis with FinancialBERT.
    """
)

# Section: Key Features
st.header("Key Features")
st.write(
    "SentimentTrader offers the following features:"
)

st.markdown(
    """
    - **Stock Price Prediction**: Predict stock prices using a combination of traditional time series forecasting and sentiment analysis.
    - **Sentiment Analysis**: Analyze sentiment from financial news headlines and descriptions, categorizing them into positive, neutral, or negative sentiments.
    - **Interactive Charts**: Visualize stock price trends, predictions, and sentiment scores through interactive charts.
    - **Time Series Forecasting**: Use Prophet to forecast future stock prices and understand underlying trends and seasonalities.
    """
)

# Section: How to Use SentimentTrader
st.header("How to Use SentimentTrader")
st.write(
    "To use SentimentTrader, follow these steps:"
)

st.markdown(
    """
    - **Select a stock ticker**: Choose the stock you want to analyze.
    - **Define the time period**: Specify the range for fetching historical data.
    - **View stock price trends and predictions**: Analyze past performance and predicted future trends.
    - **Analyze sentiment**: Examine sentiment from financial news related to the selected stock.
    - **Explore with interactive charts**: Use the interactive charts to visualize data and predictions.
    """
)