import streamlit as st
import yfinance as yf
from prophet import Prophet
import plotly.graph_objs as go
import plotly.express as px

# Function to fetch historical stock data
def fetch_stock_data(symbol, start_date, end_date):
    """Fetch historical stock data."""
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Function to prepare data for Prophet
def prepare_data(stock_data):
    """Prepare data for Prophet."""
    stock_data.reset_index(inplace=True)
    stock_data.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
    data = stock_data[['ds', 'y']]
    return data

# Function to create and fit Prophet model
def fit_prophet_model(data):
    """Create and fit Prophet model."""
    model = Prophet()
    model.fit(data)
    return model

# Function to make future predictions
def make_forecast(model, periods):
    """Make future predictions."""
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

# Function to plot forecast
def plot_forecast(data, forecast):
    """Plot historical data and forecast."""
    st.subheader('Stock Price Forecast')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['ds'], y=data['y'], mode='lines', name='Historical Data'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))
    fig.update_layout(xaxis_title='Date', yaxis_title='Price', title='AMZN Stock Price Forecast')
    st.plotly_chart(fig)

# Function to plot trend, yearly, and weekly seasonality components
def plot_components(model, forecast):
    """Plot trend, yearly, and weekly seasonality components."""
    st.subheader('Trend, Yearly, and Weekly Seasonality Components')
    fig = model.plot_components(forecast)
    st.plotly_chart(fig)

# Function to plot seasonalities in the data
def plot_seasonalities(data):
    """Plot seasonalities in the data."""
    st.subheader('Seasonalities in the Data')
    fig = px.line(data, x='ds', y='y', labels={'ds': 'Date', 'y': 'Price'}, title='Trend vs. Actual Price')
    st.plotly_chart(fig)

# Main function to run the app
def main():
    # Page title
    st.set_page_config(page_title="Market Forecast", page_icon="📈", layout="wide")
    st.title('📈 Market Prediction' )
    # Sidebar input options
    st.sidebar.title('Settings')
    symbol = st.sidebar.text_input('Enter Stock Symbol', 'AMZN')
    start_date = st.sidebar.text_input('Start Date', '2020-01-01')
    end_date = st.sidebar.text_input('End Date', '2022-01-01')

    # Fetch historical stock data
    stock_data = fetch_stock_data(symbol, start_date, end_date)

    # Prepare data for Prophet
    data = prepare_data(stock_data)

    # Create and fit Prophet model
    model = fit_prophet_model(data)

    # Make future predictions
    # Forecasting an additional 3 months (90 days)
    forecast = make_forecast(model, periods=90)

    # Plot forecast
    plot_forecast(data, forecast)

    # Plot trend, yearly, and weekly seasonality components
    plot_components(model, forecast)

    # Plot seasonalities in the data
    plot_seasonalities(data)

if __name__ == '__main__':
    main()
