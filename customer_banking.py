# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("What is your current balance in the savings account: ")
    savings_balance = input()
    savings_balance=float(savings_balance)

    print("What is the interest rate for your savings account:") 
    savings_interest = input()
    savings_interest = float(savings_interest)
    print("How many months for maturity : ")
    savings_maturity = input()
    savings_maturity = int(savings_maturity)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print (f"Your updated savings account balance is :{updated_savings_balance:.2f}")
    print (f"Interest earned for your savings account is: {interest_earned:.2f}")

    print ("-" *50)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    print("What is the starting balance for your CD account: ")
    cd_balance = input()
    cd_balance = float(cd_balance)

    print("What is the interest rate for your CD account")
    cd_interest = input()
    cd_interest = float(cd_interest)

    print("What is the duration of your CD in months")
    cd_maturity = input()
    cd_maturity = int(cd_maturity)
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print (f"Your updated CD account balance is :{updated_cd_balance:.2f}")
    print (f"Interest earned for your CD account is: {interest_earned: .2f}")

if __name__ == "__main__":
    # Call the main function.
    main()