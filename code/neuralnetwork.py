# -*- coding: utf-8 -*-
"""NeuralNetwork.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11pmDwefEMrCH-mkDPt3ayPySH7n10xbJ
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from tensorflow import keras
from tensorflow.keras import layers

# the Iris dataset
url_iris = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns_iris = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
iris = pd.read_csv(url_iris, names=columns_iris)

# Preprocess
X_iris = iris.drop('Species', axis=1)
y_iris = iris['Species']

# Encode categorical features
label_encoder_iris = LabelEncoder()
X_encoded_iris = X_iris.apply(lambda x: label_encoder_iris.fit_transform(x) if x.dtype == 'O' else x)

# One-hot encode the target variable
y_encoded_iris = to_categorical(label_encoder_iris.fit_transform(y_iris))

# Split
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_encoded_iris, y_encoded_iris, test_size=0.2, random_state=42)

# Standardize the features
scaler_iris = StandardScaler()
X_train_scaled_iris = scaler_iris.fit_transform(X_train_iris)
X_test_scaled_iris = scaler_iris.transform(X_test_iris)

# Train Neural Network
model_iris = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled_iris.shape[1],)),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')  # 3 output neurons for multi-class classification (Iris dataset has 3 classes)
])

model_iris.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model_iris.fit(X_train_scaled_iris, y_train_iris, epochs=20, batch_size=10, verbose=1)

# Evaluate
loss_iris, accuracy_iris = model_iris.evaluate(X_test_scaled_iris, y_test_iris)
print(f"Neural Network Accuracy on Iris dataset: {accuracy_iris * 100:.2f}%")

# Haberman’s Survival dataset

url_haberman = "https://archive.ics.uci.edu/ml/machine-learning-databases/haberman/haberman.data"
column_names_haberman = ["age", "year_of_treatment", "positive_lymph_nodes", "survival_status_after_5_years"]
haberman = pd.read_csv(url_haberman, names=column_names_haberman)

# Preprocess
X_haberman = haberman.drop('survival_status_after_5_years', axis=1)
y_haberman = haberman['survival_status_after_5_years']

# Split
X_train_haberman, X_test_haberman, y_train_haberman, y_test_haberman = train_test_split(X_haberman, y_haberman, test_size=0.2, random_state=42)

# Standardize the features
scaler_haberman = StandardScaler()
X_train_scaled_haberman = scaler_haberman.fit_transform(X_train_haberman)
X_test_scaled_haberman = scaler_haberman.transform(X_test_haberman)

# Train Neural Network
model_haberman = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled_haberman.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # 1 output neuron for binary classification
])

model_haberman.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model_haberman.fit(X_train_scaled_haberman, y_train_haberman, epochs=20, batch_size=10, verbose=1)

# Evaluate
loss_haberman, accuracy_haberman = model_haberman.evaluate(X_test_scaled_haberman, y_test_haberman)
print(f"Neural Network Accuracy on Haberman's Survival dataset: {accuracy_haberman * 100:.2f}%")

# Car Evaluation dataset

url_car = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"
column_names_car = ["buying_price", "maintenance_cost", "number_of_doors", "number_of_persons", "lug_boot", "safety", "decision"]
car = pd.read_csv(url_car, names=column_names_car)

# Preprocess
X_car = car.drop('decision', axis=1)
y_car = car['decision']

# Encode categorical features
label_encoder_car = LabelEncoder()
X_encoded_car = X_car.apply(lambda x: label_encoder_car.fit_transform(x) if x.dtype == 'O' else x)

# One-hot encode the target variable
y_encoded_car = to_categorical(label_encoder_car.fit_transform(y_car))

# Split
X_train_car, X_test_car, y_train_car, y_test_car = train_test_split(X_encoded_car, y_encoded_car, test_size=0.2, random_state=42)

# Standardize the features
scaler_car = StandardScaler()
X_train_scaled_car = scaler_car.fit_transform(X_train_car)
X_test_scaled_car = scaler_car.transform(X_test_car)

# Train Neural Network
model_car = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled_car.shape[1],)),
    Dense(32, activation='relu'),
    Dense(y_encoded_car.shape[1], activation='softmax')  # Output neurons based on the number of classes in 'decision'
])

model_car.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model_car.fit(X_train_scaled_car, y_train_car, epochs=20, batch_size=10, verbose=1)

# Evaluate
loss_car, accuracy_car = model_car.evaluate(X_test_scaled_car, y_test_car)
print(f"Neural Network Accuracy on Car Evaluation dataset: {accuracy_car * 100:.2f}%")

# Breast Cancer Wisconsin dataset

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
column_names = ["Sample_code_number", "Clump_thickness", "Uniformity_of_cell_size", "Uniformity_of_cell_shape",
                "Marginal_adhesion", "Single_epithelial_cell_size", "Bare_nuclei", "Bland_chromatin",
                "Normal_nucleoli", "Mitoses", "Class"]
cancer = pd.read_csv(url, names=column_names)

# Function to create a simple neural network model
def create_neural_network(input_shape):
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=input_shape),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Adjust the number of units based on your classification task
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Function to preprocess data and train the neural network
def train_neural_network(X_train, y_train, X_test, y_test):
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)
    y_test_encoded = label_encoder.transform(y_test)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    input_shape = (X_train_scaled.shape[1],)  # Input shape for the neural network

    model = create_neural_network(input_shape)
    model.fit(X_train_scaled, y_train_encoded, epochs=10, batch_size=32, validation_split=0.2)

    y_pred_prob = model.predict(X_test_scaled)
    y_pred = (y_pred_prob > 0.5).astype(int)

    accuracy = accuracy_score(y_test_encoded, y_pred)
    print(f"Neural Network Accuracy: {accuracy * 100:.2f}%")

# Preprocess
X = cancer.drop('Class', axis=1)
y = cancer['Class']

# Handle missing values
X.replace('?', pd.NA, inplace=True)
X = X.apply(pd.to_numeric, errors='coerce')

# Impute missing values
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Encode categorical features
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_imputed, y_encoded, test_size=0.2, random_state=42)

# Train Neural Network
train_neural_network(X_train, y_train, X_test, y_test)

# Poker Hands dataset

url_train = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-training-true.data"
url_test = "https://archive.ics.uci.edu/ml/machine-learning-databases/poker/poker-hand-testing.data"
column_names = ["S1", "C1", "S2", "C2", "S3", "C3", "S4", "C4", "S5", "C5", "Class"]

# Function to create a simple neural network model
def create_neural_network(input_shape):
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=input_shape),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')  # Adjust the number of units based on your classification task
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Function to preprocess data and train the neural network
def train_neural_network(X_train, y_train, X_test, y_test):
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)
    y_test_encoded = label_encoder.transform(y_test)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    input_shape = (X_train_scaled.shape[1],)  # Input shape for the neural network

    model = create_neural_network(input_shape)
    model.fit(X_train_scaled, y_train_encoded, epochs=10, batch_size=32, validation_split=0.2)

    y_pred_prob = model.predict(X_test_scaled)
    y_pred = (y_pred_prob > 0.5).astype(int)

    accuracy = accuracy_score(y_test_encoded, y_pred)
    print(f"Neural Network Accuracy: {accuracy * 100:.2f}%")

# Read training and testing data
poker_train = pd.read_csv(url_train, names=column_names)
poker_test = pd.read_csv(url_test, names=column_names)

# Concatenate training and testing data for simplicity
poker = pd.concat([poker_train, poker_test], ignore_index=True)

# Preprocess
X = poker.drop('Class', axis=1)
y = poker['Class']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Neural Network
train_neural_network(X_train, y_train, X_test, y_test)

# German Credit Dataset

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
column_names = ["Status of existing checking account", "Duration", "Credit history", "Purpose", "Credit amount",
                "Savings account/bonds", "Present employment since", "Installment rate in percentage of disposable income",
                "Personal status and sex", "Other debtors / guarantors", "Present residence since", "Property", "Age",
                "Other installment plans", "Housing", "Number of existing credits at this bank", "Telephone",
                "Foreign worker", "Credit risk"]
credit_data = pd.read_csv(url, names=column_names, sep=' ', header=None)

# Preprocess
X = credit_data.drop('Credit risk', axis=1)
y = credit_data['Credit risk']

# Encode categorical features
label_encoder = LabelEncoder()
X_encoded = X.apply(lambda x: label_encoder.fit_transform(x) if x.dtype == 'O' else x)

# One-hot encode the target variable
y_encoded = to_categorical(label_encoder.fit_transform(y))

# Split
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y_encoded, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Neural Network
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(2, activation='softmax')  # 2 output neurons for binary classification (good/bad credit)
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train_scaled, y_train, epochs=20, batch_size=10, verbose=1)

# Evaluate
loss, accuracy = model.evaluate(X_test_scaled, y_test)
print(f"Neural Network Accuracy: {accuracy * 100:.2f}%")