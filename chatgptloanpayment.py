# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:39:36 2023

@author: sherr
"""

def calculate_monthly_payment(principal, interest_rate, duration):
    r = interest_rate / 100 / 12  # Monthly interest rate
    n = duration  # Total number of months

    # Calculate the monthly payment
    monthly_payment = (principal * r * (1 + r) ** n) / ((1 + r) ** n - 1)

    return monthly_payment


# Input values
loan_amount = 12000
interest_rate = 4.6
loan_duration = 48

# Calculate the monthly payment
payment = calculate_monthly_payment(loan_amount, interest_rate, loan_duration)

# Print the result
print(f"The monthly payment for a ${loan_amount} loan at {interest_rate}% interest rate "
      f"over {loan_duration} months is ${payment:.2f}")
