from sklearn.externals import joblib


def predict(df):
    print("inside predictor\n")
    
    #import model & run prediction
    model = joblib.load("./models/estimator1.pkl")
    prediction = model.predict(df)[0]
    # print(prediction)

    lower_bound = int(prediction*.85)
    upper_bound = int(prediction*1.15)

    return lower_bound,upper_bound