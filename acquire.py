from env import host, user, password
import seaborn as sns
import pandas as pd
import numpy as np
import os

def get_connection(db, user = user, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_titanic_data():
    sql_query = 'SELECT * FROM passengers'
    df = pd.read_sql(sql_query, get_connection('titanic_db'))
    df.to_csv('titanic.csv')
    return df

def get_titanic_data(cached=False):
    if cached or os.path.isfile('titanic.csv') == False:
        df = new_titanic_data()
    else:
        df = pd.read_csv('titanic.csv', index_col=0)
    return df

def new_iris_data():
    sql_query = 'SELECT * FROM measurements AS m JOIN species USING (species_id)'
    df = pd.read_sql(sql_query, get_connection('iris_db'))
    df.to_csv('iris.csv')
    return df

def get_iris_data(cached=False):
    if cached or os.path.isfile('iris.csv') == False:
        df = new_iris_data()
    else:
        df = pd.read_csv('iris.csv', index_col=0)
    return df
