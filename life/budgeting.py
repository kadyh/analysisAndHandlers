# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:18:22 2022

@author: kdhsu24

It is so expensive to exist, but let's figure it out.
"""


#%% Class
class budgeting:
    def __init__(self):
        # empty initialize
        pass
    
    def monthlySavings(self,pay,payType,rent=0,wifi=0,gasAndElec=0,phone=0,carMaint=0,food=0,tuition=0,gas=0,meds=0,carRegDMV=0,perc401k=0,healthIns=0,dentalIns=0,eyeIns=0,liability=0,carIns=0,rentersIns=0,umbr=0,medicare=0.0145,ss=0.064,caUnemp=0.034):
        # pay: int, dollars
        # payType: string, 'hourly' 'monthly' or 'salary'
        # rent: int, rent in dollars, optional
        if payType=='hourly':
            monthly=pay*5*8*4
            salary=monthly*12
        elif payType=='monthly':
            salary=pay*12
        elif payType=='salary':
            monthly=pay/12
            salary=pay
        else:
            print('payType invalid')
            return
        fedDeduction=12550
        caDeduction=4601
        fedTaxableIncome=salary-fedDeduction-perc401k-healthIns-dentalIns-eyeIns
        stateTaxableIncome=salary-caDeduction
        if fedTaxableIncome<=9950:
            fedTax=salary*.1
        elif fedTaxableIncome>9950 and fedTaxableIncome<=40525:
            fedTax=995+0.12*(fedTaxableIncome-9950)
        elif fedTaxableIncome>40525 and fedTaxableIncome<=86375:
            fedTax=4664+0.22*(fedTaxableIncome-40525)
        elif fedTaxableIncome>86375 and fedTaxableIncome<=164925:
            fedTax=14751+0.24*(fedTaxableIncome-86375)
        elif fedTaxableIncome>164925 and fedTaxableIncome<=209425:
            fedTax=33603+0.32*(fedTaxableIncome-164925)
        if stateTaxableIncome<=9325:
            stateTax=salary*0.01
        elif stateTaxableIncome>9325 and stateTaxableIncome<=22107:
            stateTax=93.25+0.02*(stateTaxableIncome-9325)
        elif stateTaxableIncome>22107 and stateTaxableIncome<=34892:
            stateTax=348.89+0.04*(stateTaxableIncome-22107)
        elif stateTaxableIncome>34892 and stateTaxableIncome<=48435:
            stateTax=860.29+0.06*(stateTaxableIncome-34892)
        elif stateTaxableIncome>48435 and stateTaxableIncome<=61214:
            stateTax=1672.87+0.08*(stateTaxableIncome-48435)
        elif stateTaxableIncome>61214 and stateTaxableIncome<=312686:
            stateTax=2695.19+0.093*(stateTaxableIncome-61214)
        monthlyFedTax=fedTax/12
        monthlyStateTax=stateTax/12
        caUnemployment=monthly*caUnemp
        medicareCost=monthly*medicare
        socialSecurity=monthly*ss
        monthly401k=perc401k*monthly
        savings=monthly-monthlyFedTax-monthlyStateTax-rent-wifi-gasAndElec-phone-carMaint-food-tuition-gas-meds-carRegDMV--healthIns-dentalIns-eyeIns-liability-carIns-rentersIns-umbr-monthly401k
        return savings
    
