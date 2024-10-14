import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Step 1: Load Dataset (we'll use an example dataset of housing prices)
data = {
    'Area': [2100, 1600, 2400, 1410, 3000],
    'Price': [400000, 330000, 369000, 232000, 540000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Data Cleaning (Check for missing values)
print("Checking for missing values:")
print(df.isnull().sum())

# Step 3: Basic Statistics with Pandas and NumPy
print("\nBasic statistics:")
print(df.describe())

# Calculate the mean and standard deviation using NumPy
mean_area = np.mean(df['Area'])
std_area = np.std(df['Area'])
print(f"\nMean of Area: {mean_area}")
print(f"Standard Deviation of Area: {std_area}")

# Step 4: Data Visualization using Matplotlib
plt.figure(figsize=(8, 6))
plt.scatter(df['Area'], df['Price'], color='blue', label='Data Points')
plt.title('House Prices vs Area')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.show()

# Step 5: Fitting a Linear Regression Model using SciPy
# Independent variable (Area) and dependent variable (Price)
X = df['Area']
Y = df['Price']

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

# Display regression statistics
print(f"\nSlope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")

# Step 6: Plotting the Regression Line
plt.figure(figsize=(8, 6))
plt.scatter(df['Area'], df['Price'], color='blue', label='Data Points')
plt.plot(df['Area'], intercept + slope*df['Area'], color='red', label='Regression Line')
plt.title('Linear Regression: House Prices vs Area')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.legend()
plt.show()
