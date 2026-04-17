from src.extract import fetch_data
from src.validate import validate_data
from src.transform import transform_data, save_data
from src.predict import predict_next_price

def run_pipeline():
    print("--- Starting Daily Data Pipeline ---")
    
    raw_df = fetch_data()
    valid_df = validate_data(raw_df)
    final_df = transform_data(valid_df)
    
    # 3.5 Predict (Receiving TWO values now)
    print("AI is calculating tomorrow's market forecast...")
    prediction_val, accuracy_val = predict_next_price(final_df)
    
    # Save both values to the dataframe
    final_df['Prediction'] = prediction_val
    final_df['Accuracy'] = accuracy_val  # <--- NEW column
    
    # 4. Save Output
    save_data(final_df)
    
    print(f"--- Success! Forecast: ${prediction_val:,.2f} | Confidence: {accuracy_val:.1f}% ---")

if __name__ == "__main__":
    run_pipeline()
