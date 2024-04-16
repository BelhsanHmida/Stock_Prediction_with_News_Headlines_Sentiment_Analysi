import streamlit as st 

st.set_page_config(page_title="SentimentTrader", page_icon="😎" , layout="wide")

st.title('📈 SentimentTrader')
st.write(
    """
### **Predicting Stocks with Sentiment Analysis**

**SentimentTrader is an Ai-powered stock price prediction app built with Python and Streamlit. It utilizes Deep Learning models to forecast stock prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

SentimentTrader is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch financial data from Yahoo Finance API
- **Plotly** - To create interactive financial charts


"""
)