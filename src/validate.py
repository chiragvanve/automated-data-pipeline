import pandera.pandas as pa
import pandas as pd

# 1. We tell Pandera exactly what perfect data should look like
schema = pa.DataFrameSchema({
    "Date": pa.Column("datetime64[ns]"), # Must be a valid date
    "Close": pa.Column(float, checks=pa.Check.gt(0)), # Price must be greater than 0
})

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Validating data...")
    # 2. Force the data through our rules. It will crash if it fails!
    validated_df = schema.validate(df)
    return validated_df

# 3. This block lets us test it right now
if __name__ == "__main__":
    from extract import fetch_data
    
    raw_df = fetch_data()
    clean_df = validate_data(raw_df)
    
    print("Validation successful! The data is perfect.")

