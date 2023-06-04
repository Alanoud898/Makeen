from sklearn.linear_model import LinearRegression

# Sample data
height = [[140], [150], [160], [170], [180]]
shoe_size = [7, 8, 9, 10, 11]

# Create and fit the linear regression model
regression_model = LinearRegression()
regression_model.fit(height, shoe_size)

# Predict shoe size for a new height
new_height = [[165]]  # Provide the new height in centimeters
predicted_shoe_size = regression_model.predict(new_height)

print("Predicted Shoe Size:", predicted_shoe_size)
