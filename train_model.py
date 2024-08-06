#!/usr/bin/env python
# coding: utf-8

# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
iris = pd.read_csv('iris3.csv')

# View Data Types
print(iris.dtypes)

# Split into features and target
X = iris.drop(columns=['species'])
y = iris['species']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")

# Save model
joblib.dump(model, 'model.pkl')
