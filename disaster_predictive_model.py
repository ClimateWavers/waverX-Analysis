# Import necessary libraries
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import LinearRegression
from sklearn.metrics import accuracy_score


# Load disaster climate data
climate_data = pd.read_csv("dataset/climate_data.csv")


# Prepare features and labels
X = climate_data.drop(columns=["Magnitude", "Magnitude Scale"])
y = climate_data["Magnitude", "Magnitude Scale"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
lr = LinearRegression(n_estimators=100)
lr.fit(X_train, y_train)

y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)

print( y_lr_train_pred, y_lr_test_pred)
