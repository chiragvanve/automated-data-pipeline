import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_price(df):
    """
    Predicts tomorrow's price based on the last 30 days of price data.
    """
    # 1. We only care about the most recent trend (last 30 days)
    recent_data = df.tail(30).copy()
    
    # 2. Create a time index (0, 1, 2... 29) for the X-axis
    recent_data['day_index'] = np.arange(len(recent_data))
    
    # 3. Define Features (X) and Target (y)
    X = recent_data[['day_index']].values
    y = recent_data['Close'].values
    
    # 4. Initialize and train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # 5. Predict the price for tomorrow (day index 30)
    prediction = model.predict([[30]])
    
    return float(prediction[0])
