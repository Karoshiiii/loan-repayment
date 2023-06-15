# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:46:27 2023

@author: King Vann

Pst = r * PV/(1-(1+r)**-n)
Pmt is how much you pay back/mo
n is number of months
r is interest rate per month
n is number of mnths

"""
def Idunno(PV, r, n):
    """
     Parameters
    ----------
    PV : TYPE
        DESCRIPTION. present value (amt borrow)
    r : TYPE
        DESCRIPTION. interest rate APR
    n : TYPE
        DESCRIPTION. number of months to pay back loan

    Returns
    -------
    Pmt : TYPE
        DESCRIPTION. how much you pay each month

    """
    Pmt = r * PV/(1-(1+r)**-n)
    return Pmt

# input the PV
import numpy as np

n = 48
PV = input('enter PV: ')
PV = float(PV)
print(f"PV = {PV} \n")

r= input('interest APR: ')
r = float(r)/100
r = r/12
print(f"interest = {r: 0.3f}")

pmt = Idunno(PV, r,n)
pmt = np.round(pmt, 2)
print(f"payment is {pmt: } per month")
