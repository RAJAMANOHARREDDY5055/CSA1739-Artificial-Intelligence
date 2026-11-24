"""Image segmentation using K-means on pixel colours."""
from sklearn.cluster import KMeans
from PIL import Image
import numpy as np

# Put an image named input.jpg beside this script.
image = Image.open("input.jpg").convert("RGB")
pixels = np.asarray(image)
h, w, _ = pixels.shape
samples = pixels.reshape(-1, 3)
model = KMeans(n_clusters=3, random_state=0, n_init=5).fit(samples)
segmented = model.cluster_centers_[model.labels_].reshape(h, w, 3).clip(0, 255).astype("uint8")
Image.fromarray(segmented).save("segmented_output.png")
print("Saved segmented_output.png")
