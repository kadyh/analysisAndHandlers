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
    
    def doubleJoinByNewKey(self,mainDF,df2,keyCol,strDF2):
        # keyCol is a string
        mainDF=mainDF.set_index(keyCol)
        df2=df2.set_index(keyCol)
        joinedDF=mainDF.join(df2,how="outer",rsuffix=strDF2)
        return joinedDF
    
    def tripleJoinByNewKey(self,mainDF,df2,df3,keyCol,strDF2,strDF3):
        # keyCol is a string
        mainDF=mainDF.set_index(keyCol)
        df2=df2.set_index(keyCol)
        df3=df3.set_index(keyCol)
        joinedDF=mainDF.join(df2,how="outer")
        joinedDF=joinedDF.join(df3,how="outer",lsuffix=strDF2,rsuffix=strDF3)
        return joinedDF
    def anonKeysSplit(self,dfLarge,df1,df2,df3):
        #taking the large df, removing the names, and replacing them with new keys
        numKeys=len(dfLarge)
        listKeys=np.random.randint(0,numKeys*100,numKeys)
        arrayU,indexU=np.unique(listKeys,return_index=True)
        uniqueKeys=listKeys[indexU]
        while len(uniqueKeys)!=numKeys:
            needed=numKeys-len(uniqueKeys)
            neededKeys=np.random.randint(numKeys*100,numKeys*200,needed)
            uniqueKeys=np.concatenate((uniqueKeys,neededKeys))
        dfLarge['keysCol']=uniqueKeys
        dfLarge=dfLarge['keysCol']
        dfHold1=df1.merge(dfLarge,left_on='name',right_on='name')
        df1=dfHold1.drop('name',axis=1)
        df1=df1.set_index('keysCol')
        dfHold2=df2.merge(dfLarge,left_on='name',right_on='name')
        df2=dfHold2.drop('name',axis=1)
        df2=df2.set_index('keysCol')
        dfHold3=df3.merge(dfLarge,left_on='name',right_on='name')
        df3=dfHold3.drop('name',axis=1)
        df3=df3.set_index('keysCol')

     
        return df1,df2,df3

        
    
