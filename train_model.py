import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import pickle

# Load the dataset
data = pd.read_csv('insurance.csv')

# Preprocess data
data['sex'] = data['sex'].map({'male': 0, 'female': 1})
data['smoker'] = data['smoker'].map({'yes': 1, 'no': 0})
data = pd.get_dummies(data, columns=['region'], drop_first=True)

# Define features and target
X = data.drop('charges', axis=1)
y = data['charges']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(X_train, y_train)

# Save the trained model to a pickle file
with open('insurance_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as insurance_model.pkl")
