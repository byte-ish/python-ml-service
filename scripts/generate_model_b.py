# scripts/generate_model_b.py
import pickle
from sklearn.linear_model import LinearRegression

# Sample training data
X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Numerical input features
y = [6, 15, 24]  # Target output (sum of features)

# Train the regression model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
model_path = "app/models/model_b.pkl"
with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model B saved at {model_path}")