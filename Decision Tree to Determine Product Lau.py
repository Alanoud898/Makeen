# Decision Tree and Expected Value Calculation

# Define the costs and outcomes
cost_manufacture = 20  # Cost to manufacture per unit
price_sell = 40  # Selling price per unit
fixed_cost = 50000  # Fixed cost to launch the product
demand_estimate = 10000  # Estimated demand for the product

profit_high_demand = 200000  # Profit if demand is greater than or equal to 10,000 units
profit_low_demand = 100000  # Profit if demand is less than 10,000 units
no_launch_profit = 0  # Profit if the product is not launched

# Calculate the expected value of launching the product
expected_value_launch = float(demand_estimate * (profit_high_demand - cost_manufacture) +
                         (10000 - demand_estimate) * (profit_low_demand - cost_manufacture)) - fixed_cost

# Calculate the expected value of not launching the product
expected_value_no_launch = no_launch_profit

# Print the expected values
print("Expected Value (Launch): $", expected_value_launch)
print("Expected Value (No Launch): $", expected_value_no_launch)

# Make a recommendation based on the expected values
if expected_value_launch > expected_value_no_launch:
    recommendation = "Launch the product"
else:
    recommendation = "Do not launch the product"

print("Recommendation:", recommendation)
