# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 22:27:50 2022

@author: kadyh

functions:
-pullReadCSV: takes in the path of a csv and reads it into a dataframe

"""
import pandas as pd
import numpy as np
import csv
from pathlib import Path

class handlers:
    def __init__(self):
        # empty initialize
        a=1
        
    def pullReadCSV(self,pathStr):
        # To test in terminal:
            # from handlers import handlers
            # pathCompLit=r'C:\Users\kadyh\Downloads\EDUC C122 Independent Research Project I Hsu - computerLiteracyData.csv'
            # handle=handlers(pathCompLit)
        loadedCSV=pd.read_csv(pathStr)
        return loadedCSV
    
    def doubleJoinByNewKey(self,mainDF,df2,keyCol):
        # keyCol is a string
        mainDF=mainDF.set_index(keyCol)
        df2=df2.set_index(keyCol)
        joinedDF=mainDF.join(df2,how="outer")
        return joinedDF
    
    def tripleJoinByNewKey(self,mainDF,df2,df3,keyCol,strDF2,strDF3):
        # keyCol is a string
        mainDF=mainDF.set_index(keyCol)
        df2=df2.set_index(keyCol)
        df3=df3.set_index(keyCol)
        joinedDF=mainDF.join(df2,how="outer")
        joinedDF=joinedDF.join(df3,how="outer",lsuffix=strDF2,rsuffix=strDF3)
        return joinedDF
    
