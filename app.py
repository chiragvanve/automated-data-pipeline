import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Setup the Web Page
st.set_page_config(page_title="BTC Dashboard", layout="wide")
st.title("📈 Automated Bitcoin Market Dashboard")
st.markdown("This dashboard is fed by a Python data pipeline.")

# 2. Load the Cleaned Data
df = pd.read_csv("data/cleaned_data.csv")

# 3. Calculate the top KPI numbers
latest_price = df['Close'].iloc[-1]
yesterday_price = df['Close'].iloc[-2]
price_change = latest_price - yesterday_price

# 4. Draw the KPI boxes at the top
col1, col2, col3 = st.columns(3)
col1.metric("Latest Price (USD)", f"${latest_price:,.2f}", f"${price_change:,.2f}")
col2.metric("7-Day Moving Avg", f"${df['7-Day_MA'].iloc[-1]:,.2f}")
col3.metric("Latest Volume", f"{df['Volume'].iloc[-1]:,}")

# 5. Draw the Chart
st.subheader("Price Trend (Last 30 Days)")
fig = px.line(df, x='Date', y=['Close', '7-Day_MA'], 
              labels={'value': 'Price (USD)'},
              color_discrete_sequence=['#1f77b4', '#ff7f0e'])
st.plotly_chart(fig, use_container_width=True)

# 6. Show the underlying data table
st.subheader("Cleaned Data Table")
st.dataframe(df)
