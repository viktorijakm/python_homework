import matplotlib.pyplot as plt
import numpy as np

# Line Plot
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1000, 1200, 1500, 1700, 1600, 1800]
plt.plot(months, revenue, marker='o', linestyle='-', color='blue')
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.show()

# Bar Plot
categories = ["Region A", "Region B"]
sales = [500, 700]
plt.bar(categories, sales, color=['green', 'orange'])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.show()

# Histogram
random_data = np.random.randn(1000)
plt.hist(random_data, bins=30, color='purple', alpha=0.7)
plt.title("Random Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()