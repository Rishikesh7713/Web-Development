import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
iris=pd.read_csv(r"Iris Dataset.csv",
encoding="utf-8")
print(iris.head())
sb.countplot(iris["SepalLengthCm"])
plt.show()
sb.barplot(iris["Species"])
plt.show()