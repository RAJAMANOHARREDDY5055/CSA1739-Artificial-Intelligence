"""Grid-search hyperparameter tuning for an SVM classifier."""
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.2, random_state=42, stratify=y)
pipeline = make_pipeline(StandardScaler(), SVC())
grid = GridSearchCV(pipeline, {
    "svc__C": [.1, 1, 10],
    "svc__kernel": ["linear", "rbf"],
    "svc__gamma": ["scale", "auto"]
}, cv=5, scoring="accuracy")
grid.fit(Xtr, ytr)
print("Best parameters:", grid.best_params_)
print("Best CV accuracy:", grid.best_score_)
print("Test accuracy:", grid.score(Xte, yte))
