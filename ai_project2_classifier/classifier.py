
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score
import numpy as np

def load_and_prepare_data():
    """Loads the Iris dataset and prepares it for classification."""
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names
    target_names = iris.target_names

    # Split data into training and testing sets (80% train, 20% test)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)

    # Feature Scaling: Standardize features by removing the mean and scaling to unit variance
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, target_names

def train_and_evaluate_knn(X_train, X_test, y_train, y_test, target_names, k_neighbors=5):
    """Trains a KNN classifier and evaluates its performance."""
    # Initialize KNN classifier with a specified number of neighbors
    knn = KNeighborsClassifier(n_neighbors=k_neighbors)

    # Train the model using the scaled training data
    knn.fit(X_train, y_train)

    # Make predictions on the scaled test data
    y_pred = knn.predict(X_test)

    print(f"\n--- K-Nearest Neighbors (KNN) Classifier with K={k_neighbors} ---")

    # Evaluate the model
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=target_names))

    # Calculate and print F1 Score
    f1 = f1_score(y_test, y_pred, average='weighted')
    print(f"Weighted F1 Score: {f1:.2f}")

    return knn, y_pred

if __name__ == "__main__":
    print("Starting AI Project 2: Iris Classification with KNN")
    X_train, X_test, y_train, y_test, target_names = load_and_prepare_data()
    _ = train_and_evaluate_knn(X_train, X_test, y_train, y_test, target_names)

    print("\nProject 2 execution complete.")
