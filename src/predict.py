import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_price(df):
    recent_data = df.tail(30).copy()
    recent_data['day_index'] = np.arange(len(recent_data))
    
    X = recent_data[['day_index']].values
    y = recent_data['Close'].values
    
    model = LinearRegression()
    model.fit(X, y)
    
    # NEW: Calculate the R-squared score (Accuracy of trend fit)
    accuracy_score = model.score(X, y) * 100
    
    # Predict for tomorrow (index 30)
    prediction = model.predict([[30]])
    
    return float(prediction[0]), float(accuracy_score)
