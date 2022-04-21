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
    
