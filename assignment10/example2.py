import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1000, 1200, 1500, 1700, 1600, 1800]

# Customized Line Plot
plt.plot(months, revenue, marker='o', linestyle='--', color='red', linewidth=2)
plt.title("Monthly Revenue", fontsize=14, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(["Revenue"], loc="upper left")
plt.show()

categories = ["North", "South"]
sales = [2500, 1800]

# Customized Bar Plot
plt.bar(categories, sales, color=['skyblue', 'salmon'], width=0.5, edgecolor='black')
plt.title("Sales by Region", fontsize=14, fontweight='bold')
plt.xlabel("Region", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)
plt.show()