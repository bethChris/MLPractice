# train_model.py
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

print("started training")
# Train a simple model (Random Forest in this case)
model = RandomForestClassifier()
model.fit(X, y)

print("finished training the model!")
# Save the trained model to a file
joblib.dump(model, 'trained_model.joblib')
