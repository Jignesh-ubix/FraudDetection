import joblib
import pandas as pd
from utils.dbOperations import get_new_transactions

def preprocess_data(df):
    # Drop unnecessary columns
    df = df.drop(['customer', 'merchant'], axis=1)
    df['gender'] = df['gender'].apply(lambda g: 1 if g == 'M' else 0)
    return df

model = joblib.load('xgb_model.pkl')
def get_predictions(input_data):
    df = pd.DataFrame([item.model_dump() for item in input_data])
    df = preprocess_data(df)
    df['category'] = df['category'].astype('category')
    print(df)
    preds = model.predict(df)
    
    return {"predictions": preds.tolist()}

def get_new_data():
    rows = get_new_transactions()
    
    response = [{'id': row[0],
                 'customer': row[1],
                 'age': row[2],
                 'gender': row[3],
                 'merchant': row[4],
                 'category': row[5],
                 'amount': float(row[6])} for row in rows]
    
    return response