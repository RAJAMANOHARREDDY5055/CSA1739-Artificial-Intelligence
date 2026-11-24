"""User-user collaborative filtering with cosine similarity."""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Rows are users; columns are items. Zero means not rated.
ratings = np.array([
    [5, 4, 0, 1],
    [4, 5, 0, 0],
    [1, 0, 5, 4],
    [0, 1, 4, 5],
], dtype=float)
similarity = cosine_similarity(ratings)
def recommend(user, k=2):
    scores = similarity[user] @ ratings
    weights = similarity[user] @ (ratings > 0)
    estimates = scores / np.maximum(weights, 1e-9)
    estimates[ratings[user] > 0] = -1
    return np.argsort(estimates)[::-1][:k], estimates
items, estimates = recommend(0)
print("Recommended item indexes for user 0:", items.tolist())
print("Estimated ratings:", estimates[items].round(2).tolist())
