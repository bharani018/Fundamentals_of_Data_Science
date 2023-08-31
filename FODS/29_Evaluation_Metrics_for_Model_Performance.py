from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load dataset (replace this with your own dataset loading code)
data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train a model (replace this with your own model training code)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Ask user for feature and target variable names
feature_names = list(X.columns)
target_names = data.target_names

selected_features = input(f"Available features: {', '.join(feature_names)}\n"
                          f"Enter the names of the features (comma-separated): ").split(',')

selected_target = input(f"Available target classes: {', '.join(target_names)}\n"
                        f"Enter the name of the target variable: ")

# Evaluate the model
y_pred = model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

# Display evaluation metrics
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
