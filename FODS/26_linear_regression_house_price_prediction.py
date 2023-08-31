from sklearn.linear_model import LinearRegression

# Sample dataset of houses with features and prices
# You can replace this with your actual dataset
# Format: [area, bedrooms, location] -> price
dataset = [
    [1400, 3, 'SuburbA', 250000],
    [1200, 2, 'SuburbB', 220000],
    [1600, 4, 'SuburbC', 280000],
    [1000, 2, 'SuburbB', 190000],
    [1800, 3, 'SuburbA', 300000]
]

# Separate features and prices
X = [[house[0], house[1]] for house in dataset]
y = [house[3] for house in dataset]

# Initialize Linear Regression model
model = LinearRegression()

# Train the model on the dataset
model.fit(X, y)

# Input new house features
area = float(input("Enter area (sq. ft.): "))
bedrooms = int(input("Enter number of bedrooms: "))

# Predict the price of the new house
new_house = [[area, bedrooms]]
predicted_price = model.predict(new_house)

print(f"The predicted price of the new house is: ${predicted_price[0]:,.2f}")
