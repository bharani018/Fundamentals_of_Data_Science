import pandas as pd
import scipy.stats as stats

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('customer_data.csv')  # Replace with your dataset filename

# Calculate sample mean and standard error
sample_mean = data['rating'].mean()
standard_error = data['rating'].std() / (len(data)**0.5)

# Choose confidence level and calculate critical value
confidence_level = 0.95
degrees_of_freedom = len(data) - 1
critical_value = stats.t.ppf((1 + confidence_level) / 2, df=degrees_of_freedom)

# Calculate confidence interval
lower_bound = sample_mean - (critical_value * standard_error)
upper_bound = sample_mean + (critical_value * standard_error)

print(f"Sample Mean: {sample_mean:.2f}")
print(f"Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")


