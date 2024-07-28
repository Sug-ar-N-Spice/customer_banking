"""Import the Account class from the Account.py file."""
    # ADD YOUR CODE HERE
from Account import Account

            # Define a function for the Savings Account
            # """Creates a savings account, calculates interest earned, and updates the account balance.
            #     Args:
            #         balance (float): The initial savings account balance.
            #         interest_rate (float): The APR interest rate for the savings account.
            #         months (int): The length of months to determine the amount of interest.

            #     Returns:
            #         float: The updated savings account balance after adding the interest earned.
            #         And returns the interest earned.
            #     """



def create_savings_account(balance, interest_rate, months):
    # Create an instance of the Account class with the initial balance and interest rate
    account = Account(balance, interest_rate)

    # Calculate interest earned
    interest = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    balance += interest

    # Pass the updated balance to the set_balance method using the instance of the Account class
    account.set_balance(balance)

    # Pass the interest earned to the set_interest method using the instance of the Account class
    account.set_interest(interest)

    # Return the updated balance and interest earned
    return account.balance, account.interest

