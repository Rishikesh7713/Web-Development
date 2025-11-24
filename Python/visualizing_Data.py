import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
weather=pd.read_csv(r"Weather Dataset - Trial Activity DataSet.csv.csv",
encoding="utf-8")
print(weather.head())
sb.countplot(weather["weather_type"])
plt.show()
sb.barplot(x=weather["humidity"],y=weather["temperature"])
plt.show()
