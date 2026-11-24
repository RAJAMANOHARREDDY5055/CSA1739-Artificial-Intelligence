"""Principal Component Analysis on Iris data."""
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X, y = load_iris(return_X_y=True)
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
reduced = pca.fit_transform(X_scaled)
print("Original shape:", X.shape)
print("Reduced shape:", reduced.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("First five reduced rows:\n", reduced[:5])
