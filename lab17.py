import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df4 = pd.read_csv("prog16a.csv", header=None)
df4.columns = ['experience_level', 'salary_in_usd']

plt.figure(figsize=(8,5))
plt.bar(df4['experience_level'], df4['salary_in_usd'],
        width=0.5, edgecolor='white', linewidth=0.4)

plt.xlabel("Experience Level")
plt.ylabel("Salary (USD)")
plt.title("Salary vs Experience Level (Matplotlib)")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x='experience_level', y='salary_in_usd', data=df4)

plt.title("Average Salary by Experience Level (Seaborn)")
plt.show()
