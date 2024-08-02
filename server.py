from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load the trained model
model = joblib.load('iris_model.pkl')

# Define the class names for Iris
class_names = ['setosa', 'versicolor', 'virginica']

# Define request body model
class Features(BaseModel):
    features: list[float]

@app.get("/")
def foo():
    return {
        "status": "Iris-Flower classification Application"
    }

@app.post('/predict')
def predict(data: Features):
    # Extract features
    features = np.array([data.features])
    
    # Make prediction
    prediction = model.predict(features)
    predicted_class = class_names[prediction[0]]
    
    # Return the result
    return {'class': predicted_class}
