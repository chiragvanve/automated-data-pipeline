from src.extract import fetch_data
from src.validate import validate_data
from src.transform import transform_data, save_data
from src.predict import predict_next_price  # <--- NEW: Intelligence module

def run_pipeline():
    print("--- Starting Daily Data Pipeline ---")
    
    # 1. Extract
    raw_df = fetch_data()
    
    # 2. Validate
    valid_df = validate_data(raw_df)
    
    # 3. Transform & Clean
    final_df = transform_data(valid_df)
    
    # 3.5 Predict (The Intelligence Layer)
    print("AI is calculating tomorrow's market forecast...")
    prediction_val = predict_next_price(final_df)
    
    # We save the prediction as a column so the CSV carries it to your dashboard
    final_df['Prediction'] = prediction_val
    
    # 4. Save Output
    save_data(final_df)
    
    print(f"--- Success! Tomorrow's Predicted Price: ${prediction_val:,.2f} ---")

if __name__ == "__main__":
    run_pipeline()
