import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error
from sklearn.impute import KNNImputer
import pickle

def predict(new_data):
    # impute missing `Overall Qual` values
    imp_data = pd.read_csv('./streamlit_imp_data.csv')
    imp = KNNImputer()
    imp.fit(imp_data)
    shaped_data = np.reshape(new_data, (1, -1)) # to configure data format as if it is a new row to existing data
    input_data = imp.transform(shaped_data) # impute missing value
    # load model
    with open('final_model.sav','rb') as f:
        model = pickle.load(f)
    pred = model.predict([input_data][0])
    return pred 
