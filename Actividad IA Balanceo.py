# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eHah17_SpiAYIWl6mNMg-OMQg9siScL2
"""

from sklearn.datasets import make_classification
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from google.colab import drive
drive.mount('/content/drive')

# Generate imbalanced data
X, y = make_classification(n_samples=43400, n_features=2, n_classes=2,
                           n_informative=2, n_redundant=0, n_repeated=0,
                           weights=[0.9, 0.1], random_state=42)
data = pd.DataFrame(X, columns=["Feature1", "Feature2"])
data["Target"] = y

database= pd.read_csv('/content/drive/MyDrive/dataset.csv')


# Visualize the imbalanced data
print("Class distribution (imbalanced):")
print(database["hypertension"].value_counts())
plt.scatter(database["age"], database["avg_glucose_level"], c=database["hypertension"], cmap="coolwarm", alpha=0.6)
plt.title("Original Imbalanced Data")
plt.xlabel("Age")
plt.ylabel("Average Glucose Level")
plt.show()

# Split data
X_train, X_test, y_train, y_test = train_test_split(database[["age", "avg_glucose_level"]],
                                                    database["hypertension"], test_size=0.3, random_state=42)

# Train model on imbalanced data
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Classification Report (Imbalanced Model):")
print(classification_report(y_test, y_pred))

# Apply SMOTE to balance the data
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Visualize the balanced data
print("Class distribution (balanced):")
print(pd.Series(y_resampled).value_counts())

# Convert resampled data back to DataFrame for visualization (if needed)
X_resampled = pd.DataFrame(X_resampled, columns=X_train.columns)

# Visualize balanced data
plt.scatter(X_resampled["age"], X_resampled["avg_glucose_level"], c=y_resampled, cmap="coolwarm", alpha=0.6)
plt.title("SMOTE-Balanced Data")
plt.xlabel("Age")
plt.ylabel("Average Glucose Level")
plt.show()

# Train model on balanced data
model.fit(X_resampled, y_resampled)
y_pred_resampled = model.predict(X_test)
print("Classification Report (Balanced Model):")
print(classification_report(y_test, y_pred_resampled))

print(" \n \nHow did the model's performance change after balancing the data? \n")
print(" \n The model's performance after applying SMOTE (oversampling) improved in terms of metrics that account for the minority class, such as recall or F1-score. \n")
print(" \n \nWhich technique (oversampling or undersampling) was more effective, and why? \n")
print(" \n This scenario uses oversampling (SMOTE), where synthetic examples for the minority class are generated. \n Undersampling would remove samples from the majority class to achieve balance, but this could lead to significant loss of information, especially when the dataset is imbalanced to the extent that 90% of the data belongs to the majority class. \n \n")
print(" \n \nWhich metrics are most useful for evaluating models in problems with imbalanced classes?\n")
print(" \n In problems with imbalanced classes, standard accuracy is not always meaningful because the model might predict the majority class overwhelmingly well while ignoring the minority class. \n Metrics that focus on the minority class and provide a more nuanced evaluation include: \n 1. Precision \n 2. Recall \n 3. F1-Score \n ")

