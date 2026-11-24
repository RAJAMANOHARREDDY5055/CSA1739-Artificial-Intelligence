"""Support Vector Machine for binary classification."""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, random_state=42, stratify=y)
model = make_pipeline(StandardScaler(), SVC(kernel="rbf"))
model.fit(Xtr, ytr)
print("Accuracy:", accuracy_score(yte, model.predict(Xte)))
