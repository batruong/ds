import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

def plot( house_data):
    plt.plot(house_data['price'], house_data['surface'], 'ro', markersize=4)
    plt.show()
    return;
def print_( house_data ):
    for index, row in house_data.iterrows():
        print row["price"], row["surface"], row["arrondissement"]
    return;
def clean_old( house_data ):
    return house_data[house_data.price.notnull() & house_data.surface.notnull() & house_data.arrondissement.notnull()];
def clean( house_data ):
    return house_data.dropna();
def linearRegression_1( house_data_raw ):
    # Linear Regresssion No Arrondissement
    # Cleaning
    house_data_raw_clean = clean(house_data_raw)
    # Column Selection
    house_data_1 = house_data_raw_clean[['price','surface']]
    # Train Test
    house_data_1_train, house_data_1_test = train_test_split(house_data_1, train_size=0.8)
    # Train Test Surface Price
    house_data_1_train_surface = house_data_1_train.surface.values.reshape(-1,1)
    house_data_1_train_price = house_data_1_train.price.values.reshape(-1,1)
    house_data_1_test_surface = house_data_1_test.surface.values.reshape(-1,1)
    house_data_1_test_price = house_data_1_test.price.values.reshape(-1,1)
    rl = linear_model.LinearRegression()
    rl.fit(house_data_1_train_surface, house_data_1_train_price)
    house_data_1_predicted_price = rl.predict(house_data_1_test_surface)
    # Prediciton Error
    mean_squared_error_ = mean_squared_error(house_data_1_test_price, house_data_1_predicted_price)
    variance_score = r2_score(house_data_1_test_price, house_data_1_predicted_price)
    coefficient = rl.coef_
    print("Mean squared error: %.2f"  % mean_squared_error_)
    print('Variance score: %.2f' % variance_score)
    print('Coefficients: %.2f', coefficient)
    # Plot
    plt.plot( house_data_1_train_surface, house_data_1_train_price,'ro', markersize=4)
    plt.plot( house_data_1_test_surface, house_data_1_predicted_price,'b', markersize=4)
    plt.show()
    return ;
house_data_raw = pd.read_csv('house_data.csv')
linearRegression_1(house_data_raw)




"""
plt.plot(house_data_raw['price'], house_data_raw['surface'], 'ro', markersize=4)
plt.show()
"""
"""
price = house_data_raw['price']
surface = house_data_raw['surface']

from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(surface, price)
# regr.predict(donnee_test)
"""
