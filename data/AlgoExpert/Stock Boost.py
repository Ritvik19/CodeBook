import xgboost as xgb

def stock_boost(X_train, y_train, X_test):
    return xgb.XGBClassifier().fit(X_train.drop('sector', axis=1), y_train).predict(X_test.drop('sector', axis=1))
    
