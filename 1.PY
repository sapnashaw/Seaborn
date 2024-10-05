#1. Create a scatter plot to visualize the relationship between two variables, by generating a synthetic
#dataset.

import numpy as np
import matplotlib.pyplot as plt

# Generating synthetic data
np.random.seed(42)
x_synthetic = np.random.rand(100) * 100  # 100 random values for x between 0 and 100
y_synthetic = 3 * x_synthetic + (np.random.randn(100) * 50)  # y has a linear relation to x with added noise

# Creating a scatter plot for the synthetic data
plt.scatter(x_synthetic, y_synthetic, color='blue')

# Adding labels and title
plt.title('Scatter Plot of Synthetic Data')
plt.xlabel('X values')
plt.ylabel('Y values')

# Display the plot
plt.show()


 