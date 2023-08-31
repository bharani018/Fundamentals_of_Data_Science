import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Suppress the warning about feature names
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)

# Load the customer dataset from a CSV file
customer_data = pd.read_csv('customer.csv')

# Extract the shopping-related features for clustering
features = customer_data.drop('CustomerID', axis=1)

# Normalize the features using StandardScaler
scaler = StandardScaler()
normalized_features = scaler.fit_transform(features)

# Number of clusters
num_clusters = 4

# Perform K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(normalized_features)

# Input new customer's features
new_customer_features = []
for i in range(len(features.columns)):
    feature = float(input(f"Enter feature {i+1} for the new customer: "))
    new_customer_features.append(feature)
new_customer_features = np.array(new_customer_features).reshape(1, -1)

# Normalize the new customer's features
normalized_new_customer = scaler.transform(new_customer_features)

# Assign the new customer to a cluster
cluster_assignment = kmeans.predict(normalized_new_customer)

print(f"The new customer is assigned to cluster {cluster_assignment[0]}")
