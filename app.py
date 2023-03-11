# Initialize the order details in three separate lists
order_food_names = ["Pizza", "Salad", "Soup"]
order_food_price = [75.00,   45.00,  15.00]
order_food_q = [2,       1,      2]

# Initialize a variable to hold the total cost of the order
total_cost = 0.0

# Loop through each item in the order
for i in range(len(order_food_names)):
    # Calculate the cost of the current item by multiplying its price and quantity
    item_cost = order_food_price[i] * order_food_q[i]
    # Add the item cost to the running total of the order cost
    total_cost += item_cost
    # Print the details of the current item, including its index, name, price, quantity, and cost
    print(i+1, order_food_names[i],
          order_food_price[i], order_food_q[i], item_cost)

# Print the total cost of the order after all items have been processed
print("Total cost:", total_cost)