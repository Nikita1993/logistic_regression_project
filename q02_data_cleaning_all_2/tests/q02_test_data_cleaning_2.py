import pandas as pd
from unittest import TestCase
from ..build import data_cleaning_2
from greyatomlib.logistic_regression_project.q02_data_cleaning_all.build import data_cleaning
from greyatomlib.logistic_regression_project.q01_outlier_removal.build import outlier_removal
from inspect import getfullargspec

loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)
loan_data = outlier_removal(loan_data)
X, y, X_train, X_test, y_train, y_test = data_cleaning(loan_data)
X_train, X_test, y_train, y_test = data_cleaning_2(X_train, X_test, y_train, y_test)
train_val = X_train['Dependents_1'].value_counts()
train_val1 = X_train['Property_Area_Urban'].value_counts()
test_val = X_test['Property_Area_Urban'].value_counts()
test_val1 = X_test['Dependents_1'].value_counts()

class TestData_cleaning_2(TestCase):
    def test_data_cleaning_2_arguments(self):

        # Input parameters tests
        args = getfullargspec(data_cleaning_2)
        self.assertEqual(len(args[0]), 4, "Expected arguments %d, Given %d" % (4, len(args[0])))
        
    def test_data_cleaning_2_defaults(self):
        args = getfullargspec(data_cleaning_2)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
        
    def test_data_cleaning_2_return_type_X_test(self):
        self.assertIsInstance(X_test, pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(X_test)))

    def test_data_cleaning_2_return_type_X_train(self):
        self.assertIsInstance(X_train, pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(X_train)))

    def test_data_cleaning_2_return_type_y_train(self):
        self.assertIsInstance(y_train, pd.core.series.Series,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(y_train)))

    def test_data_cleaning_2_return_type_y_test(self):
        self.assertIsInstance(y_test, pd.core.series.Series,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(y_test)))

        # Return value tests
    def test_data_cleaning_2_return_value_train(self):    
        self.assertEqual(list(train_val), [343, 65], "Return value counts does not match expected value counts")

    def test_data_cleaning_2_return_value_train1(self):
        self.assertEqual(list(train_val1), [277, 131], "Return value counts does not match expected value counts")

    def test_data_cleaning_2_return_value_test(self):
        self.assertEqual(list(test_val), [87, 50], "Return value counts does not match expected value counts")

    def test_data_cleaning_2_return_value_test1(self):
        self.assertEqual(list(test_val1), [114, 23], "Return value counts does not match expected value counts")

    def test_data_cleaning_2_return_shape_X_train(self):
        self.assertEqual(X_train.shape, (408, 14), "Return value shape does not match expected value")

    def test_data_cleaning_2_return_shape_X_test(self):
        self.assertEqual(X_test.shape, (137, 14), "Return value shape does not match expected value")