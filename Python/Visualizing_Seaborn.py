import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
weather=pd.read_csv(r"Tips Dataset.csv",
encoding="utf-8")
print(weather.head())
sb.countplot(weather["size"])
plt.show()
sb.barplot(x=weather["tip"],y=weather["total_bill"])
plt.show()
