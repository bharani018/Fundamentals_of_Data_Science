import numpy as np
import pandas as pd

data = pd.read_csv('company.csv')
products = pd.DataFrame(data)
print(products)

products.index = ['jan', 'feb', 'mar']


mean_columns = np.mean(products, axis=1)
print(mean_columns)
allprod = np.mean(mean_columns)
print(allprod)

arr = products.to_numpy()
arr.shape = (3, 3)
print(arr)
