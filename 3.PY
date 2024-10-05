#3. Create a dataset representing categories and their corresponding values. Compare different categories
#   based on numerical values.

import matplotlib.pyplot as plt

# Creating a dataset representing categories and their corresponding values
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [35, 50, 20, 45, 30]

# Creating a bar chart to compare the categories
plt.bar(categories, values, color='orange')

# Adding labels and title
plt.title('Comparison of Categories Based on Values')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the bar chart
plt.show()
