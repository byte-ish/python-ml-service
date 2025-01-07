# scripts/generate_model_a.py
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Sample training data
texts = [
    "I love this product",
    "This is amazing",
    "I hate this",
    "This is bad"
]
labels = ["positive", "positive", "negative", "negative"]

# Create a pipeline with vectorizer and classifier
pipeline = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Train the model
pipeline.fit(texts, labels)

# Save the model
model_path = "app/models/model_a.pkl"
with open(model_path, "wb") as file:
    pickle.dump(pipeline, file)

print(f"Model A saved at {model_path}")