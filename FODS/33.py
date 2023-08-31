import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the car dataset
# Replace 'car_data.csv' with your actual data file path
dataset = pd.read_csv('car_data.csv')

# Select features and target
selected_features = ['engine_size', 'horsepower', 'fuel_efficiency']
target = 'price'

X = dataset[selected_features]
y = dataset[target]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate model evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared: {r2:.2f}")

# Get coefficients to understand feature importance
coefficients = model.coef_
feature_importance = dict(zip(selected_features, coefficients))
sorted_feature_importance = sorted(
    feature_importance.items(), key=lambda x: x[1], reverse=True)
print("Feature Importance:")
for feature, importance in sorted_feature_importance:
    print(f"{feature}: {importance:.2f}")
