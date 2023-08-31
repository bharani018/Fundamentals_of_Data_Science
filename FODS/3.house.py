'''3'''

import pandas as pd
import numpy as np

a = pd.read_csv("house.csv")


b = a[a['no_of_bed']>4]
print(b)

#sales prize average


print('Average sale price of  houses with more than four bedrooms: ')
m= np.mean(b['sale_price'])
print(m)
