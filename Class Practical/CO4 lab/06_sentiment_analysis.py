"""Basic sentiment analysis with TF-IDF and logistic regression."""
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "I love this product", "Excellent service and very happy",
    "This is wonderful", "Amazing experience",
    "I hate this", "Very bad and disappointing",
    "Terrible service", "The product is awful"
]
labels = ["positive"] * 4 + ["negative"] * 4
model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(texts, labels)
for sentence in ["I love the excellent service", "This is terrible"]:
    print(sentence, "=>", model.predict([sentence])[0])
