"""Linear regression on a generated continuous dataset."""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

rng = np.random.default_rng(7)
X = np.arange(1, 51).reshape(-1, 1)
y = 3.5 * X.ravel() + 8 + rng.normal(0, 5, size=50)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)
print("Slope:", model.coef_[0], "Intercept:", model.intercept_)
print("MSE:", mean_squared_error(y_test, pred), "R2:", r2_score(y_test, pred))
print("Prediction for X=60:", model.predict([[60]])[0])
