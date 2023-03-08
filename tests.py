import pdb 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from concepts import Debt 

# Step 1. Test that the debt operations all work as intended. 
def test_debt_compound(): 
    """
        Simulate a simplified compounding of a debt over 1 period 
    """
    
    debt1 = Debt(earner='earner_1', 
                 name='LOC_1', 
                 balance=10000, 
                 limit=20000, 
                 prime_rate=0.05, 
                 apr=0.10, 
                 is_floating=True, 
                 repayment_frequency='monthly', 
                 repayment_date=1, 
                 repayment_principle_prct=0.01, 
                 repayment_interest_prct=1.00, 
                 revolving=True)


    # Apply 1 compounding period. 
    debt1.compound()
    
    # Verify that the new balance, available credit, annual interest, and daily interest amounts are correct.     
    assert debt1.balance == 10000 + 10000*0.10/12
    assert debt1.available_credit == 20000 - (10000 + 10000*0.10/12)    
    assert debt1.annual_interest == (10000 + 10000*0.10/12)*0.10
    assert debt1.daily_interest == (10000 + 10000*0.10/12)*0.10/365
    assert debt1.credit_utilization == (10000 + 10000*0.10/12)/20000

    return None 
    
def test_debt_payment(): 
    """
       Simulate a debt payment     
    """
    
    debt1 = Debt(earner='earner_1', 
                 name='LOC_1', 
                 balance=10000, 
                 limit=20000, 
                 prime_rate=0.05, 
                 apr=0.10, 
                 is_floating=True, 
                 repayment_frequency='monthly', 
                 repayment_date=1, 
                 repayment_principle_prct=0.01, 
                 repayment_interest_prct=1.00, 
                 revolving=True)

    # Apply a payment of $1000.00
    debt1.payment(1000)
    
    # Verify that the balance, available credit, annual and daily interest rate fees are correct 
    assert debt1.balance == 9000
    assert debt1.available_credit == 11000
    assert debt1.annual_interest == 9000*0.10 
    assert debt1.daily_interest == 9000*0.10/365
    assert debt1.credit_utilization == 9000/20000
    
def test_normal_widthdrawal(): 
    """
        Simulate a withdrawal from the credit source, when the withdrawal is under the available credit limit 
    """
    
    debt1 = Debt(earner='earner_1', 
                 name='LOC_1', 
                 balance=9000, 
                 limit=20000, 
                 prime_rate=0.05, 
                 apr=0.10, 
                 is_floating=True, 
                 repayment_frequency='monthly', 
                 repayment_date=1, 
                 repayment_principle_prct=0.01, 
                 repayment_interest_prct=1.00, 
                 revolving=True)

    # Apply a withdrawl of $1000.00 
    withdrawn_amount = debt1.withdrawal(1000)
    
    # Verify that balance, available credit, annual and daily interest amounts are correct 
    assert withdrawn_amount == 1000
    assert debt1.balance == 10000
    assert debt1.available_credit == 10000
    assert debt1.annual_interest == 10000*0.1 
    assert debt1.daily_interest == 10000*0.1/365  
    assert debt1.credit_utilization == 10000/20000

def test_max_overdraw():
    debt1 = Debt(earner='earner_1', 
                 name='LOC_1', 
                 balance=20000, 
                 limit=20000, 
                 prime_rate=0.05, 
                 apr=0.10, 
                 is_floating=True, 
                 repayment_frequency='monthly', 
                 repayment_date=1, 
                 repayment_principle_prct=0.01, 
                 repayment_interest_prct=1.00, 
                 revolving=True)

    # Apply a test withdrawal 
    withdrawn_amount = debt1.withdrawal(1000)
    
    assert withdrawn_amount == 0 
    assert debt1.balance == 20000
    assert debt1.available_credit == 0 
    assert debt1.annual_interest == 20000*0.1
    assert debt1.daily_interest == 20000*0.1/365
    assert debt1.credit_utilization == 1 

def test_overdraw_with_limit_available(): 
    debt1 = Debt(earner='earner_1', 
                 name='LOC_1', 
                 balance=19000, 
                 limit=20000, 
                 prime_rate=0.05, 
                 apr=0.10, 
                 is_floating=True, 
                 repayment_frequency='monthly', 
                 repayment_date=1, 
                 repayment_principle_prct=0.01, 
                 repayment_interest_prct=1.00, 
                 revolving=True)
    
    # Apply a test withdrawal 
        
    withdrawn_amount = debt1.withdrawal(2000)
    
    assert withdrawn_amount == 1000
    assert debt1.balance == 20000
    assert debt1.available_credit == 0 
    assert debt1.annual_interest == 20000*0.1
    assert debt1.daily_interest == 20000*0.1/365
    assert debt1.credit_utilization == 1

def test_positive_credit_limit_change(): 
    debt1 = Debt(earner='earner_1', 
                 name='LOC_1', 
                 balance=10000, 
                 limit=20000, 
                 prime_rate=0.05, 
                 apr=0.10, 
                 is_floating=True, 
                 repayment_frequency='monthly', 
                 repayment_date=1, 
                 repayment_principle_prct=0.01, 
                 repayment_interest_prct=1.00, 
                 revolving=True)
    
    # Apply 5000 credit limit increase 
    debt1.credit_limit_change(5000)
    
    assert debt1.limit == 25000
    assert debt1.credit_utilization == 10000/25000
    
def test_negative_credit_limit_change(): 
    debt1 = Debt(earner='earner_1', 
                 name='LOC_1', 
                 balance=10000, 
                 limit=20000, 
                 prime_rate=0.05, 
                 apr=0.10, 
                 is_floating=True, 
                 repayment_frequency='monthly', 
                 repayment_date=1, 
                 repayment_principle_prct=0.01, 
                 repayment_interest_prct=1.00, 
                 revolving=True)
    
    # Apply 5000 credit limit increase 
    debt1.credit_limit_change(-5000)
    
    assert debt1.limit == 15000
    assert debt1.credit_utilization == 10000/15000
    
# NEXT STEP: Add safeguards to ensure credit limit cannot fall below 0, or below available balance for revolving debts. 