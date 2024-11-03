# Customer Banking Program for Savings and CD Accounts

## Overview

This program is designed to help users calculate the interest earned on both savings and certificate of deposit (CD) accounts based on their initial balances, interest rates, and maturity periods. Users input their account details, and the program calculates and displays the interest earned and the updated balance.

## File Structure
The program assumes the following module structure:

**cd_account.py:** Contains the create_cd_account function, which calculates the interest and balance update for a CD account.

**savings_account.py:** Contains the create_savings_account function, which calculates the interest and balance update for a savings account.

**main.py:** The main program file where user inputs are taken and results are displayed.

## Program Workflow
**Savings Account Calculation:**

Prompts the user to enter the balance, interest rate, and maturity period (in months) for a savings account.
Calls create_savings_account to calculate the interest earned and update the balance based on user input.
Displays the interest earned and the updated balance.

**CD Account Calculation:**

Prompts the user to enter the balance, interest rate, and maturity period (in months) for a CD account.
Calls create_cd_account to calculate the interest earned and update the balance based on user input.
Displays the interest earned and the updated balance.
