from src.extract import fetch_data
from src.validate import validate_data
from src.transform import transform_data, save_data

def run_pipeline():
    print("--- Starting Daily Data Pipeline ---")
    
    # 1. Extract
    raw_df = fetch_data()
    
    # 2. Validate
    valid_df = validate_data(raw_df)
    
    # 3. Transform & Clean
    final_df = transform_data(valid_df)
    
    # 4. Save Output
    save_data(final_df)
    
    print("--- Pipeline Execution Successful! ---")

if __name__ == "__main__":
    run_pipeline()
