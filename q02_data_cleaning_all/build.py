# %load q02_data_cleaning_all/build.py
# Default Imports
#import sys, os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from logistic_regression_project.q01_outlier_removal.build import outlier_removal
import random as rand
loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)
loan_data = outlier_removal(loan_data)

rand.seed(9)
# Write your solution here :
def data_cleaning(df):
    X= df.iloc[:,:-1]
    y=df['Loan_Status']
    X_tain,X_test,y_train,y_test= train_test_split(X, y, test_size=0.25, random_state=9)
    return X,y,X_tain,X_test,y_train,y_test



