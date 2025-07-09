import uvicorn
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from functions import get_predictions, get_new_data

class InferenceInput(BaseModel):
    customer: str
    age: float
    gender: str
    merchant: str
    category: str
    amount: float

app = FastAPI(title="Fraud Detection API",
              description="API for predicting fraud in transactions")

@app.post('/predict')
def predict(input_data: List[InferenceInput]):
    """Detect fraud in transactions based on input data.

    Args:
        input_data (List[InferenceInput]): It will be list objects having below keys:
        - customer: str
        - age: float
        - gender: str
        - merchant: str
        - category: str
        - amount: float

    Returns:
        dict: Return predictions in a dictionary format with key "predictions" and value as a list of predictions.
    """
    # Convert input to DataFrame
    
    return get_predictions(input_data)

@app.get('/get_new_transactions')
def get_new_transactions():
    return get_new_data()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
