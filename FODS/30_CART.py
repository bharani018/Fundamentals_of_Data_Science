import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Load the car dataset
df = pd.read_csv("car.csv")

# Create the CART model
model = DecisionTreeRegressor(max_depth=3)

# Fit the model to the data
model.fit(df.drop("Price", axis=1), df["Price"])

# Get the user input for the new car features
mileage = float(input("\nEnter the mileage of the new car: "))
age = float(input("\nEnter the age of the new car (in years): "))
brand = input(f"\nAvailable cars :\n 1-Toyota 2-Honda 3-Ford 4-Chevy 5-Nissan 6-BMW 7-Mercedes 8-Audi 9-Lexus 10-Tesla\n 11-Volvo 12-Land Rover 13-Jeep 14-Chrysler 15-Dodge 16-GMC 17-Buick 18-Acura 19-Infiniti 20-Mazda\n"f"Enter the brand of the new car: ")
engine_type = input(
    f"\nEngine Types :\n 1-Gas 2-Diesel 3-Hybrid 4-Electric 5-Other\n "f"Enter the engine type of the new car: ")

# Predict the price of the new car
predicted_price = model.predict([[mileage, age, brand, engine_type]])[0]

# Print the predicted price
print("The predicted price of the new car is: $", predicted_price)
