import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor 
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import math

class Model:

    def __init__(self,datafile='cleaned_turbine_data.xlsx'):
        self.df=pd.read_excel('cleaned_turbine_data.xlsx')
        self.df.set_index('TimeStamp',inplace=True)
        self.df=self.df.drop(columns='Comp Inlet Temp')
        self.regressor=DecisionTreeRegressor()

    def split(self):
        X=self.df.loc[:,'Exhaust temp':'Comp discharge temp']
        y=self.df.loc[:,'Generated watts']
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    def fit(self):
        self.model=self.regressor.fit(self.X_train,self.y_train)
    
    def predict(self,input_value):
        if input_value==None:
            y_pred=self.regressor.predict(self.X_test)
            print("R_squared: " + str(round(r2_score(self.y_test,y_pred),4)))
            return y_pred
        else:
            result=self.regressor.predict(np.array([input_value]))
            return result





def calculate_generated_power(input_data):
    model=Model()
    model.split()
    model.fit()
    # input_value=[1100.11,57.32,113.05,644.57]
    return model.predict(input_data)

