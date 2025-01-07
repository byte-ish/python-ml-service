# scripts/generate_model_b.py
import pickle
from sklearn.base import BaseEstimator, TransformerMixin

# Custom sum model
class SumModel(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def predict(self, X):
        return [sum(x) for x in X]

# Instantiate and save the model
model = SumModel()

model_path = "app/models/model_b.pkl"
with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model B saved at {model_path}")