import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

# 1. Page Config & Professional Styling
st.set_page_config(page_title="Aero Bitcoin Analytics", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for a minimalist "Glassmorphism" look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; font-weight: 700; color: #00d4ff; }
    div[data-testid="stMetricLabel"] { font-size: 1rem; color: #9eaab1; }
    section[data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stPlotlyChart { border: 1px solid #30363d; border-radius: 10px; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar - Currency & Model Health
st.sidebar.title("💎 Global Settings")
currency_choice = st.sidebar.selectbox("Market Currency", ["USD", "INR", "EUR", "GBP"])

# Currency Mapping
currency_symbols = {"USD": "$", "INR": "₹", "EUR": "€", "GBP": "£"}
curr_symbol = currency_symbols[currency_choice]

# Fetch Real-time Exchange Rate (USD to Choice)
@st.cache_data(ttl=3600)
def get_exchange_rate(target):
    if target == "USD": return 1.0
    ticker = f"USD{target}=X"
    data = yf.Ticker(ticker).fast_info['last_price']
    return data

rate = get_exchange_rate(currency_choice)

# 3. Load & Process Data
df = pd.read_csv("data/cleaned_data.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Apply Exchange Rate to Prices
for col in ['Close', '7-Day_MA', 'Prediction']:
    df[col] = df[col] * rate

latest_price = df['Close'].iloc[-1]
yesterday_price = df['Close'].iloc[-2]
price_change = latest_price - yesterday_price
prediction_val = df['Prediction'].iloc[-1]
accuracy_val = df['Accuracy'].iloc[-1]

# 4. Sidebar - Intelligence Section
st.sidebar.divider()
st.sidebar.subheader(" AI Model Intelligence")
st.sidebar.metric("Trend Confidence", f"{accuracy_val:.1f}%")
st.sidebar.progress(accuracy_val / 100)

if accuracy_val > 80:
    st.sidebar.success("Strong Trend Reliability")
else:
    st.sidebar.warning("Volatile Market Conditions")

# 5. Header Area
st.title("Bitcoin Market Dashboard")
st.caption(f"Real-time pipeline analysis | Base Currency: {currency_choice}")
st.divider()

# 6. KPI Grid (The 4 Main Metrics)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Latest Market Price", f"{curr_symbol}{latest_price:,.2f}", f"{curr_symbol}{price_change:,.2f}")

with col2:
    # Adding a color indicator for the forecast
    delta_forecast = prediction_val - latest_price
    st.metric(" 24h Prediction", f"{curr_symbol}{prediction_val:,.2f}", f"{curr_symbol}{delta_forecast:,.2f}")

with col3:
    st.metric("7-Day Moving Avg", f"{curr_symbol}{df['7-Day_MA'].iloc[-1]:,.2f}")

with col4:
    st.metric("Trade Volume", f"{df['Volume'].iloc[-1]:,.0f}")

st.divider()

# 7. Professional Charting
st.subheader("Market Momentum (Last 30 Days)")
fig = px.area(df, x='Date', y='Close', 
              labels={'Close': f'Price ({currency_choice})'},
              template="plotly_dark",
              color_discrete_sequence=['#00d4ff'])

fig.add_scatter(x=df['Date'], y=df['7-Day_MA'], name="7-Day Trend", line=dict(color="#ff7f0e", width=2))

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig, use_container_width=True)

# 8. Data Inspecter
with st.expander("📁 View Raw Data"):
    st.dataframe(df.sort_values(by='Date', ascending=False), use_container_width=True)
