"""K-means clustering on generated 2D points."""
import numpy as np
from sklearn.cluster import KMeans

rng = np.random.default_rng(2)
points = np.vstack([
    rng.normal([0, 0], .7, (40, 2)),
    rng.normal([4, 4], .7, (40, 2)),
    rng.normal([0, 5], .7, (40, 2))
])
model = KMeans(n_clusters=3, random_state=2, n_init=10).fit(points)
print("Cluster centers:\n", model.cluster_centers_)
print("First 15 labels:", model.labels_[:15])
