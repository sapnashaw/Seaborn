#5. Generate a synthetic dataset with correlated features. Visualize the correlation matrix of a dataset using a
#   heatmap.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate synthetic data with correlated features
np.random.seed(42)
n_samples = 100

# Create a synthetic dataset with correlated features
x1 = np.random.rand(n_samples)
x2 = x1 * 0.5 + np.random.rand(n_samples) * 0.5  # x2 is correlated with x1
x3 = x1 * 0.2 + np.random.rand(n_samples) * 0.8  # x3 is less correlated with x1
x4 = np.random.rand(n_samples)  # x4 is not correlated with x1

# Combine into a DataFrame
data = pd.DataFrame({
    'Feature 1': x1,
    'Feature 2': x2,
    'Feature 3': x3,
    'Feature 4': x4
})

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Matrix Heatmap')
plt.show()
