import matplotlib.pyplot as plt

# Data
items = ['Food', 'Clothing', 'Transport', 'Rent', 'Entertainment']
amounts = [35, 20, 21, 100, 50]

# Create bar chart
plt.bar(items, amounts, color='skyblue')

# Add titles and labels
plt.title("My Weekly Expenses")
plt.xlabel("Items")
plt.ylabel("Amount Spent($)")

# Show grid lines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the chart
plt.show()
