import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Sample dataset (replace with your actual dataset)
data = np.array([[1, 2, 0],
                 [3, 4, 1],
                 [5, 6, 0],
                 [7, 8, 1]])
X = data[:, :-1]  # Features
y = data[:, -1]   # Labels

# User input for new patient's features
new_patient_features = [float(input(f"Enter feature {i+1}: ")) for i in range(X.shape[1])]

# User input for the number of neighbors (k)
k = int(input("Enter the number of neighbors (k): "))

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
new_patient_scaled = scaler.transform([new_patient_features])

# Create and fit the KNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_scaled, y)

# Predict the label for the new patient
prediction = knn_classifier.predict(new_patient_scaled)

if prediction[0] == 0:
    print("Prediction: No condition")
else:
    print("Prediction: Condition")
