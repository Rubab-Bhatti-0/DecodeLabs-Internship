
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_user_skills():
    """Gets user input for skills and ensures at least three skills are provided."""
    skills = []
    print("\nWelcome to the Tech Stack Recommender!\n")
    print("Please enter at least three skills or interests you have, one by one.")
    print("Type 'done' when you are finished.\n")

    while True:
        skill = input(f"Enter skill {len(skills) + 1} (or 'done'): ").strip()
        if skill.lower() == 'done':
            if len(skills) < 3:
                print("Please enter at least three skills to get meaningful recommendations.")
            else:
                break
        elif skill:
            skills.append(skill)
    return skills

def recommend_tech_stacks(user_skills, raw_skills_path='raw_skills.csv', top_n=3):
    """Recommends tech stacks based on user skills using TF-IDF and cosine similarity."""
    try:
        df = pd.read_csv(raw_skills_path)
    except FileNotFoundError:
        print(f"Error: The file '{raw_skills_path}' was not found. Please ensure it's in the correct directory.")
        return []

    # Combine all skill columns into a single string for each job role
    df['combined_skills'] = df.apply(lambda row: ' '.join(row.dropna().astype(str).tolist()[1:]), axis=1)

    # Initialize TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english', sublinear_tf=True)
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_skills'])
    user_skills_str = ' '.join(user_skills)
    user_tfidf = tfidf_vectorizer.transform([user_skills_str])
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    top_n_indices = cosine_similarities.argsort()[-top_n:][::-1]

    # Get the recommended job roles and their similarity scores
    recommendations = []
    for i in top_n_indices:
        recommendations.append({
            'job_role': df.loc[i, 'job_role'],
            'similarity_score': cosine_similarities[i]
        })

    return recommendations

if __name__ == "__main__":
    user_input_skills = get_user_skills()
    if user_input_skills:
        print("\nCalculating recommendations...")
        recommendations = recommend_tech_stacks(user_input_skills)

        if recommendations:
            print("\nHere are your top tech stack recommendations:\n")
            for i, rec in enumerate(recommendations):
                print(f"{i+1}. {rec['job_role']} (Similarity: {rec['similarity_score']:.2f})")
        else:
            print("No recommendations could be generated. Please try again with different skills.")

