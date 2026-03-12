import numpy as np
from sklearn.linear_model import LinearRegression

def train_model():

    X = np.array([[1000],[1200],[1500],[1800],[2000]])
    y = np.array([200000,250000,300000,350000,400000])

    model = LinearRegression()
    model.fit(X,y)

    return model