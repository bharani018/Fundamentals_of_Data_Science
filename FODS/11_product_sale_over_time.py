import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales_Values': [1000, 690, 2900, 340, 2000, 1900, 2800, 2500, 900, 700, 2000, 1800]
}
dataframe_data = pd.DataFrame(data)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(dataframe_data['Sales_Values'])
plt.subplot(1, 3, 2)
plt.scatter(dataframe_data['Month'], dataframe_data['Sales_Values'])
plt.subplot(1, 3, 3)
plt.bar(dataframe_data['Month'], dataframe_data['Sales_Values'])
plt.tight_layout()
plt.show()
