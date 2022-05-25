# -*- coding: utf-8 -*-
"""
Created on May 24 2022

@author: kdhsu24
"""

#%% Import
import pandas as pd
import numpy as np
import csv
from budgeting import budgeting
#%% Initialize
def main():
    budget=budgeting()
    monthlySavings=budget.monthlySavings(pay=75000, payType='salary',rent=1600,wifi=75,gasAndElec=60,phone=25,carMaint=20,food=350,tuition=0,gas=400,meds=20,carRegDMV=15,perc401k=0.15,healthIns=300,dentalIns=30,eyeIns=30,liability=150,carIns=0,rentersIns=20,umbr=10,medicare=0.0145,ss=0.064,caUnemp=0.034)
    
    
    return monthlySavings

        
if __name__ == "__main__":
    monthlySavings75=main()