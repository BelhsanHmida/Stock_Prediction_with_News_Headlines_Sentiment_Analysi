import streamlit as st
import pandas as pd

trending_companies_data = {
    'Company': ['AMAZON', 'FACEBOOK', 'TESLA'],
    'Trend': ['+2.5', '-5.6', '+6.7'],
    'Price': [100, 150, 120]  # Add prices for demonstration
} 
 
# Convert the data to DataFrame
trending_companies_df = pd.DataFrame(trending_companies_data)

red_color = '#ff0000'  # Red color
green_color = '#00ff00'  # Green color

# Function to add vertical space
def add_space(num_lines):
    for _ in range(num_lines):
        st.write("\n")

# Function to apply color based on trend
def apply_color(trend):
    trend_float = float(trend[1:])
    if trend_float > 0:
        return f'background-color: {green_color}; color: black'  # Green color
    elif trend_float < 0:
        return f'background-color: {red_color}; color: black'  # Red color
    else:
        return ''

# Function to add arrow icons to trend values
def add_arrow(trend):
    arrow = ''
    if trend.startswith('+'):
        arrow = u'\u2191'  # Up arrow
    elif trend.startswith('-'):
        arrow = u'\u2193'  # Down arrow
    return f'{arrow} {trend}'

# App title
st.title("Stock Price Prediction with Sentiment Analysis 🚀")
add_space(2)

# Layout columns
left_column, _, right_column = st.columns([2, 5, 1])

# Refresh button to reset the app
if right_column.button("Refresh", key='refresh_button', help="Click to reset the app"):
    st.experimental_rerun()
add_space(1)

# Trending companies table
trending_companies_data = {
    'Company': ['AMAZON', 'FACEBOOK', 'TESLA'],
    'Trend': ['+2.5', '-5.6', '+6.7'],
    'Price': [100, 150, 120]  # Add prices for demonstration
}

# Convert the data to DataFrame
trending_companies_df = pd.DataFrame(trending_companies_data)

# Apply color to the "Trend" column
trending_companies_df['Trend'] = trending_companies_df['Trend'].apply(add_arrow)

# Display the table with custom styling
st.subheader("Trending Compaanies")
st.write(trending_companies_df.style.applymap(apply_color, subset=['Trend']), unsafe_allow_html=True)
add_space(3)
st.markdown("---")
# Input fields for company name and time window
company_name = st.text_input("Enter A Company Name:")
add_space(1)
time_window = st.selectbox("Select Time Window:", ["1 Month", "3 Months", "6 Months", "1 Year"])

# Historical data table
historical_data_data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Close Price': [100, 110, 105],
    'Volume': [1000, 1200, 900]
}
historical_data_df = pd.DataFrame(historical_data_data)

add_space(2)
st.subheader("Historical Data")
st.write(historical_data_df, unsafe_allow_html=True)
add_space(2)

# Time series graphs placeholder
st.subheader("Historical Data")
st.write('Here Time series Graphs')

# Recent tweets table
recent_tweets_data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Tweet': ['Tweet 1', 'Tweet 2', 'Tweet 3']
}
recent_tweets_df = pd.DataFrame(recent_tweets_data)

add_space(2)
st.subheader("Recent Tweets")
 
st.write(recent_tweets_df, unsafe_allow_html=True)
# Forecast button
left_column, _, right_column = st.columns([2, 1.5, 1])
if _.button("Forecast", key='forecast_button', help="Click to generate forecast"):
    # Add code to generate forecast here
    st.write("Forecast generated.")
