# AI Project 2: Iris Classifier with K-Nearest Neighbors (KNN)

This project demonstrates a basic supervised learning task: classifying the Iris dataset using the K-Nearest Neighbors (KNN) algorithm. It covers data loading, preprocessing (scaling), splitting into training and testing sets, model training, and evaluation.

## Project Structure

- `classifier.py`: The main Python script that implements the classification logic.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- numpy

You can install the necessary libraries using pip:

```bash
pip install pandas scikit-learn numpy
```

## How to Run

To execute the classifier, navigate to the project directory and run the main script:

```bash
python classifier.py
```

The script will load the Iris dataset, preprocess it, train a KNN model, and then print the confusion matrix, classification report, and F1 score for evaluation.

## How it Works

1.  **Data Loading and Preparation**: The Iris dataset is loaded. Features are scaled using `StandardScaler` to ensure all features contribute equally to distance calculations. The dataset is then split into an 80% training set and a 20% testing set, with stratification to maintain class proportions.
2.  **Model Training**: A K-Nearest Neighbors classifier is initialized (with `k=5` by default) and trained on the scaled training data.
3.  **Prediction**: The trained model makes predictions on the unseen, scaled test data.
4.  **Evaluation**: The model's performance is assessed using a confusion matrix, a detailed classification report (including precision, recall, and support for each class), and the weighted F1 score, which provides a balanced measure of the model's accuracy.
