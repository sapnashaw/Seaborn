#1. Create a scatter plot to visualize the relationship between two variables, by generating a synthetic
#   dataset.

import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(0)  # For reproducibility
x = np.random.rand(100) * 10  # 100 random x values between 0 and 10
y = 2.5 * x + np.random.normal(0, 1, 100)  # y is linearly related to x with some noise

# Create a scatter plot
plt.scatter(x, y, color='blue', alpha=0.6)

# Adding labels and title
plt.title('Scatter Plot of Synthetic Data')
plt.xlabel('X values')
plt.ylabel('Y values')

# Show the plot
plt.grid(True)
plt.show()
