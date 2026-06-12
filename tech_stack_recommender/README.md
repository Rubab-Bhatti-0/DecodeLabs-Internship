# Tech Stack Recommender

This project is a simple recommendation system that suggests the most relevant tech stacks and job roles based on user-provided skills. It uses **TF-IDF (Term Frequency-Inverse Document Frequency)** for feature extraction and **Cosine Similarity** to calculate the alignment between user interests and predefined job profiles.

## Project Structure

- `recommender.py`: The main script that takes user input and generates recommendations.
- `raw_skills.csv`: The dataset containing job roles and their associated skills.
- `test_recommender.py`: A script to test the recommendation logic with sample data.

## Requirements

- Python 3.x
- pandas
- scikit-learn

You can install the dependencies using pip:

```bash
pip install pandas scikit-learn
```

## How to Run

To start the recommender, run the following command in your terminal:

```bash
python recommender.py
```

Follow the on-screen instructions to enter at least three skills or interests. The system will then display the top 3 job roles that match your profile.

## How it Works

1. **Ingestion**: The system captures user skills through a command-line interface.
2. **Scoring**: It converts the job role dataset and the user's input into a shared vector space using TF-IDF. It then calculates the cosine similarity score between the user vector and each job role vector.
3. **Sorting**: The job roles are sorted in descending order based on their similarity scores.
4. **Filtering**: The system displays the top 3 highest-scoring recommendations to the user.
