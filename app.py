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

# --- NEW: Pull the AI Prediction ---
# We take the value from the last row of the 'Prediction' column
prediction_val = df['Prediction'].iloc[-1]
# -----------------------------------

# 4. Draw the KPI boxes at the top (Expanded to 4 columns)
col1, col2, col3, col4 = st.columns(4)

col1.metric("Latest Price (USD)", f"${latest_price:,.2f}", f"${price_change:,.2f}")

# --- NEW: Prediction Metric ---
col2.metric("🚀 AI Forecast (Tomorrow)", f"${prediction_val:,.2f}")
# ------------------------------

col3.metric("7-Day Moving Avg", f"${df['7-Day_MA'].iloc[-1]:,.2f}")
col4.metric("Latest Volume", f"{df['Volume'].iloc[-1]:,}")

# 5. Draw the Chart
st.subheader("Price Trend (Last 30 Days)")
fig = px.line(df, x='Date', y=['Close', '7-Day_MA'], 
              labels={'value': 'Price (USD)'},
              color_discrete_sequence=['#1f77b4', '#ff7f0e'])
st.plotly_chart(fig, use_container_width=True)

# 6. Show the underlying data table
st.subheader("Cleaned Data Table")
st.dataframe(df)
