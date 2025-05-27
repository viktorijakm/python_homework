import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset: This dataset is 
titanic = sns.load_dataset("titanic")

# Heat map of correlations
plt.figure(figsize=(10, 6))
correlation_matrix = titanic.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Pair Plot
sns.pairplot(titanic, vars=["age", "fare", "adult_male"], hue="survived", palette="Set2")
plt.title("Pair Plot of Age, Fare, and Survival")
plt.show()