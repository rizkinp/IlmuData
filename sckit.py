# import sklearn
# sklearn.__version__
# from sklearn.datasets import load_breast_cancer
# import pandas as pd
# import numpy as np

# data_bc = load_breast_cancer()
# df_bc = pd.DataFrame(data_bc['data'], columns=data_bc['feature_names'])
# df_bc.head()
# print(df_bc.head())
# print(data_bc['target_names'])
# from sklearn.linear_model import LinearRegression

# X = data_bc['data']
# y = data_bc['target']


# # Now you can create a LinearRegression model
# model_lr = LinearRegression()

# model_lr.fit(X, y)
# print("Coeficients:", model_lr.coef_)
# print("Intercept:", model_lr.intercept_)
# y_pred = model_lr.predict(X)
# print("Predicted values:", y_pred)

from sklearn.datasets import load_breast_cancer # import dataset breast_cancer
from sklearn.linear_model import LinearRegression # import algoritma Linear Regression
from sklearn.model_selection import train_test_split # import train/test split
from sklearn.metrics import mean_absolute_error # import mean absolute error (MAE)
from sklearn.metrics import mean_squared_error # import mean squared error

# load dataset boston
bc = load_breast_cancer()

#mendefinisikan atribut dan target
X = bc['data']
y = bc['target']

#membagi data menjadi train set dan test set untuk evaluasi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# memodelkan atribut dan target dengan Linear Regression
model_lr = LinearRegression()
model_lr.fit(X_train, y_train) # melatih model dengan data X_train dan y_train
y_predict = model_lr.predict(X_test) # menguji model dengan data X_test

# menghitung MAE dan MSE untuk melihat kinerja model
print('MAE: ', mean_absolute_error(y_predict, y_test))
print('MSE: ', mean_squared_error(y_predict, y_test))
