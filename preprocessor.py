import statsmodels.api as sm
from sklearn.externals import joblib


def preprocess(df):
    print("inside preProcess")
    
    #import scaler & scale variables
    scaler = joblib.load("./models/scaler.pkl")
    data_scaled = scaler.transform(df)
    
    #add constant
    data_proccessed =  sm.add_constant(data_scaled)

    return data_proccessed



