"""A simple feed-forward neural network using NumPy (XOR example)."""
import numpy as np
np.random.seed(1)
X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
y = np.array([[0],[1],[1],[0]], dtype=float)
W1 = np.random.randn(2, 4) * 0.5
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 1) * 0.5
b2 = np.zeros((1, 1))
sigmoid = lambda z: 1 / (1 + np.exp(-z))
for epoch in range(12000):
    h = sigmoid(X @ W1 + b1)
    out = sigmoid(h @ W2 + b2)
    error = out - y
    d2 = error * out * (1-out)
    dW2 = h.T @ d2 / len(X); db2 = d2.mean(axis=0, keepdims=True)
    d1 = (d2 @ W2.T) * h * (1-h)
    dW1 = X.T @ d1 / len(X); db1 = d1.mean(axis=0, keepdims=True)
    W2 -= 1.0*dW2; b2 -= 1.0*db2
    W1 -= 1.0*dW1; b1 -= 1.0*db1
print("Predictions:")
print(np.round(sigmoid(sigmoid(X @ W1 + b1) @ W2 + b2), 3))
