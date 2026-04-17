import pandas as pd
import os

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Transforming and cleaning data...")
    
    # 1. Keep only the columns we actually care about
    clean_df = df[['Date', 'Close', 'Volume']].copy()
    
    # 2. Add some analytics: Calculate a 7-day moving average
    clean_df['7-Day_MA'] = clean_df['Close'].rolling(window=7).mean()
    
    # 3. Round the prices to 2 decimal places so they look clean on the dashboard
    clean_df['Close'] = clean_df['Close'].round(2)
    clean_df['7-Day_MA'] = clean_df['7-Day_MA'].round(2)
    
    return clean_df

def save_data(df: pd.DataFrame, filepath: str = "data/cleaned_data.csv"):
    print(f"Saving data to {filepath}...")
    # Ensure the data folder exists before saving
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)

# This block lets us test the whole chain right now
if __name__ == "__main__":
    from extract import fetch_data
    from validate import validate_data
    
    raw = fetch_data()
    valid = validate_data(raw)
    final_df = transform_data(valid)
    
    save_data(final_df)
    print("Transformation complete! CSV saved.")
