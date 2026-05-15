import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib


data = {
    'url_length': [20, 120, 35, 150, 50, 180, 22, 210],
    'dots': [1, 6, 2, 8, 1, 9, 1, 10],
    'hyphens': [0, 5, 1, 7, 0, 9, 0, 11],
    'has_https': [1, 0, 1, 0, 1, 0, 1, 0],
    'label': [0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['url_length', 'dots', 'hyphens', 'has_https']]
y = df['label']

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(model, 'phishing_model.pkl')

print("Model trained successfully!")