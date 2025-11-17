import pandas
data={"group1":[2,5,7],"group2":[6,5,7],"group3":[6,5,9]}
df=pandas.DataFrame(data)

print("All the Groups and Details :")
print(df)
print("\n")

print("Highest Point in Each Group :")
highest_group=df.max()
print(highest_group)
print("\n")

print("Lowest Point in Each Group :")
lowest_group=df.min()
print(lowest_group)
print("\n")