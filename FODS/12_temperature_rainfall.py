import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Rainfall': [50, 60, 70, 80, 100, 120, 150, 140, 130, 100, 80, 60],
    'Temperatures': [15, 17, 20, 25, 28, 30, 32, 31, 29, 26, 22, 18]
}
city_weather = pd.DataFrame(data)

plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
plt.plot(city_weather['Months'], city_weather['Temperatures'])
# plt.plot(city_weather['Months'], city_weather['Temperatures'], marker='o', linestyle='-',
#          color='b', label='Temperature (°C)')

# plt.title('Monthly Temperature Data')
# plt.xlabel('Month')
# plt.ylabel('Temperature (°C)')
# plt.grid(True)
plt.subplot(1, 2, 2)
plt.scatter(city_weather['Months'], city_weather['Rainfall'])
# plt.scatter(city_weather['Months'], city_weather['Rainfall'], marker='o', linestyle='-',
#             color='b', label='Rainfall (mm)')

# plt.title('Monthly Rainfall Data')
# plt.xlabel('Month')
# plt.ylabel('Rainfall (mm)')
# plt.grid(True)
plt.tight_layout()
plt.show()
