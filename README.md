# customer_banking

# CD account information,Interest Earned, Updated balances (after a specified number of months).
Background
You'll be creating a customer banking system that allows users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balances after a specified number of months.

Files
Download the following files to help you get started:

Module 3 Challenge filesLinks to an external site.

Before You Begin
Before starting the assignment, be sure to complete the following steps:

Create a new repository for this project called customer_banking. Do not add this homework assignment to an existing repository.

Clone the new repository to your computer.

Inside your local Git repository, add the starter files from your file downloads.

Push these changes to GitHub or GitLab.

Challenge Instructions
The starter files consist of the following files: Accounts.py, savings_account.py, cd_account.py, and customer_banking.py. The Accounts.py file contains the Account class with methods to set the balance and interest.

In the savings_account.py file, you will import the Account class and create a create_savings_account function that will create a savings account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the cd_account.py file, you will import the Account class and create a create_cd_account function that will create a CD account instance, calculate the interest earned based on user input, update the account balance with the earned interest, and return the updated balance and interest earned.

In the customer_banking.py file, you will import the create_savings_account and create_cd_account functions, then create a main function that prompts the user to enter the savings and CD account details, call the corresponding functions to calculate the interest earned and update the balances, and display the results.

Create the Savings Account Function
Open the savings_account.py file, and do the following:

Imports the Account class from the Accounts.py file.

In the create_savings_account function do the following:

Create an instance of the Account class and pass in the balance and interest parameters.

Calculate interest earned.

HINT
Update the savings account balance by adding the interest earned.

HINT
Pass the updated balance to the set balance method using the instance of the Account class.

Pass the interest earned to the set interest method using the instance of the Account class.

Return the updated balance and interest earned.

Create the CD Account Function
Open the cd_account.py file, and do the following:

Import the Account class from the Accounts.py file.

In the create_cd_account function, do the following:

Create an instance of the Account class and pass in the parameters.

Calculate interest earned.

Update the savings account balance by adding the interest earned.

HINT
Pass the updated balance to the set balance method using the instance of the Account class.

Pass the interest earned to the set interest method using the instance of the Account class.

Return the updated balance and interest earned.

Create the Main Function
Open the customer_banking.py file, and do the following:

Import the create_cd_account and create_savings_account functions from the appropriate files.

In the main function, do the following:

Prompt the user to set the savings balance, interest rate, and months for the savings account.

HINT
Call the create_savings_account function and pass in the variables from the user.

Print out the interest earned and updated savings account balance with interest earned for the given months.

Prompt the user to set the CD balance, interest rate, and months for the CD account.

HINT
Call the create_cd_account function and pass the variables to the function used to prompt the user from the user.

Print out the interest earned and updated CD account balance with interest earned for the given months.

Call the main function.

Hints and Considerations
Consider what you've learned so far. You’ve learned how to create and import functions, pass arguments and variables into functions, refactor code, create and import class, create class methods, and instances.

If you're struggling with how to start, consider creating one Python file that has all the functions first, then separate the functions into different files. Also, look back on some of the activities you did in class. Finally, you can use pseudocoding to help you write out the steps.

Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed README.md file.

Requirements
Create the Savings Account Function (35 points)
The Account class from the Accounts.py file is imported. (4 points)

In the create_savings_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. (6 points)

The interest earned is calculated and assigned to a variable. (4 points)

The savings account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)

The updated balance is passed to the set balance method using the instance of the Account class. (6 points)

The interest earned is passed to the set balance method using the instance of the Account class. (6 points)

The updated balance and interest earned are returned by the function. (5 points)

Create the CD Account Function (35 points)
The Account class from the Accounts.py file is imported. (4 points)

In the create_cd_account function, an instance of the Account class is created and the balance and interest parameters are passed to the Account class. (6 points)

The interest earned is calculated and assigned to a variable. (4 points)

The CD account balance is updated by adding the interest earned to the balance and assigned to a variable. (4 points)

The updated balance is passed to the set balance method using the instance of the Account class. (6 points)

The interest earned is passed to the set balance method using the instance of the Account class. (6 points)

The updated balance and interest earned are returned by the function. (5 points)

Create the Main Function (30 points)
The user is prompted to set the savings balance, interest rate, and months for the savings account. (8 points)

Code is written to print out the interest earned and updated savings account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)

The user is prompted to set the savings balance, interest rate, and months for the CD account. (8 points)

Code is written to print out the interest earned and updated CD account balance with interest earned for the given months. The values are formatted to two decimal places and thousandths. (6 points)

The main function is called to run the program. (2 points)