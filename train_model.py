import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading dataset...")

# Load dataset
df = pd.read_csv("data/bollywood_movies.csv")

# Fill missing values with empty string
df = df.fillna("")

# Print column names (for debugging)
print("Columns in dataset:", df.columns)

# Create combined text safely
combined_columns = []

# Add columns only if they exist
for col in ["Genre", "Director", "Cast"]:
    if col in df.columns:
        combined_columns.append(df[col])

# Combine available columns
df["combined_features"] = ""

for col in combined_columns:
    df["combined_features"] += col + " "

print("Creating TF-IDF matrix...")

# Convert text into numerical vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined_features"])

# Compute similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix)

print("Saving model...")

# Save model
joblib.dump({
    "data": df,
    "similarity": similarity_matrix
}, "model/bollywood_model.pkl")

print("✅ Model training completed successfully!")