import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from LearningAlgorithms import ClassificationAlgorithms
import seaborn as sns
import itertools
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
import seaborn as sns


# Plot settings
plt.style.use("fivethirtyeight")
plt.rcParams["figure.figsize"] = (20, 5)
plt.rcParams["figure.dpi"] = 100
plt.rcParams["lines.linewidth"] = 2

df = pd.read_pickle("D:/ML_GYM_Tracker/data/interim/03_data_features.pkl")
# --------------------------------------------------------------
# Create a training and test set
# --------------------------------------------------------------
df_train = df.drop(columns=["participants", "category", "set"], axis=1)
X = df_train.drop(columns=["label"], axis=1)
y = df_train["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

fig, ax = plt.subplots(1, 2)
sns.countplot(x="label", data=df_train, ax=ax[0], palette="lightblue")
sns.countplot(x=y_train, ax=ax[1])
sns.countplot(x=y_test, ax=ax[1])
ax[0].set_title("Total")
ax[1].set_title("Train and Test")
plt.show()
# --------------------------------------------------------------
# Split feature subsets
# --------------------------------------------------------------


# --------------------------------------------------------------
# Perform forward feature selection using simple decision tree
# --------------------------------------------------------------


# --------------------------------------------------------------
# Grid search for best hyperparameters and model selection
# --------------------------------------------------------------


# --------------------------------------------------------------
# Create a grouped bar plot to compare the results
# --------------------------------------------------------------


# --------------------------------------------------------------
# Select best model and evaluate results
# --------------------------------------------------------------


# --------------------------------------------------------------
# Select train and test data based on participant
# --------------------------------------------------------------


# --------------------------------------------------------------
# Use best model again and evaluate results
# --------------------------------------------------------------


# --------------------------------------------------------------
# Try a simpler model with the selected features
# --------------------------------------------------------------







