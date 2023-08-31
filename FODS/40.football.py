import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a = pd.read_csv('FOOTBALL.csv')
print("Player with most number of goals: ")
c = a.sort_values(by='no_of_goals', ascending=False)
print(c.head())

print("High paid players")
s = a.sort_values(by='salary', ascending=False)
print(s.head())

m = np.mean(a['age'])
print(m)

x = a[a['age'] > m]
print(x)

z = ['LW','RW','ST','CAM','CDM','CM','CB','LB','RB','GK']
pc = a['position '].value_counts()

plt.bar(z,pc)
plt.xlabel("position")
plt.ylabel("count")
plt.show()
