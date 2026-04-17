import yfinance as yf
import pandas as pd

def fetch_data():
    print("Fetching Bitcoin data...")
    # 1. Use .history() instead of .download() to guarantee a flat table
    ticker = yf.Ticker("BTC-USD")
    data = ticker.history(period="1mo")
    
    # 2. Make Date a normal column
    data = data.reset_index()
    
    # 3. Strip timezones from the Date so Pandera doesn't crash
    data['Date'] = pd.to_datetime(data['Date']).dt.tz_localize(None)
    
    return data

if __name__ == "__main__":
    df = fetch_data()
    print(df.head())
    print("Extraction complete!")
