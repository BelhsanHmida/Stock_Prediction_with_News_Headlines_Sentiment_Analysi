# Stock_Market_Prediction_with_News_Headlines_Sentiment_Analysis

This project that combines stock price prediction with sentiment analysis. It consists of two main components: a Jupyter notebook for exploring stock data and headline data, and a Streamlit app for real-time stock price prediction using AI-based sentiment analysis.

## Table of Contents
- [Overview](#overview)
- [Jupyter Notebook Research](#jupyter-notebook-research)
- [Streamlit App](#streamlit-app)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

## Overview
SentimentTrader aims to predict stock prices by integrating traditional time series forecasting with sentiment analysis of financial news headlines. This approach helps investors make data-driven decisions based on both historical stock data and the sentiment derived from financial news.

## Jupyter Notebook Research
The Jupyter notebook in this repository explores stock price data and financial news headlines. Here's a breakdown of the key sections:

1. **Importing Libraries**: The notebook starts by importing essential libraries, including Pandas, NumPy, YFinance, Seaborn, Matplotlib, and others.

2. **Fetching Stock Data**: It uses `yfinance` to fetch historical stock data from Yahoo Finance. The notebook sets the start and end dates to define the period for analysis.

3. **Fetching News Headlines**: The notebook fetches a dataset of financial news headlines from a Kaggle source. It cleans and preprocesses the data, ensuring proper formatting and handling of missing values.

4. **Sentiment Analysis**: The notebook uses `NLTK` and `TextBlob` for basic sentiment analysis on the news headlines. It also employs the `Transformers` library with FinancialBERT for advanced sentiment analysis. This section adds sentiment scores to the news data.

5. **Stock Price Prediction with Prophet**: The notebook uses Facebook's Prophet to create a time series forecasting model. It explores trends, seasonality, and makes predictions for future stock prices.

6. **Combining Stock Data with Sentiment Scores**: The notebook merges the stock price data with the sentiment scores derived from the news headlines. It explores how sentiment affects stock prices and uses these additional features to improve the accuracy of predictions.

## Streamlit App
The Streamlit app provides a user-friendly interface for real-time stock price prediction. It allows users to:
- Select a stock ticker for analysis.
- Define the time period to fetch historical data.
- View stock price trends and predictions.
- Analyze sentiment from financial news headlines.
- Explore the impact of sentiment on stock prices through interactive charts.

The Streamlit app uses `yfinance` to fetch stock data, `Plotly` for interactive charts, and `Prophet` for stock price forecasting. It integrates the sentiment scores derived from the Jupyter notebook to enhance predictions.

## Technologies Used
- **Python**: The core programming language for both the Jupyter notebook and Streamlit app.
- **Streamlit**: Framework for creating interactive web apps.
- **YFinance**: Library to fetch stock data from Yahoo Finance.
- **Plotly**: Library for creating interactive charts.
- **Pandas**: Library for data manipulation and analysis.
- **NLTK, TextBlob, Transformers**: Libraries for sentiment analysis.
- **Prophet**: Time series forecasting tool developed by Facebook.

# Use Localy

1. Clone this Repository on your local machine
2. Create a virtual environment `conda create -n venv python=3.8` 
3. Activate it `conda activate venv`
4. Install initial deps `pip install requirements.txt`
5. Run the app `😎_About.py`

