"""Decision tree for a simple binary classification dataset."""
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

X, y = load_breast_cancer(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=.25, random_state=10, stratify=y)
model = DecisionTreeClassifier(max_depth=4, random_state=10).fit(Xtr, ytr)
pred = model.predict(Xte)
print("Accuracy:", accuracy_score(yte, pred))
print("Confusion matrix:\n", confusion_matrix(yte, pred))
