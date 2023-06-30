#!/usr/bin/python3

from file3 import *
# Create a bank database
database = BankDatabase()

# Create some accounts
account1 = Account("A001", 1000.0)
account2 = Account("A002", 500.0)
account3 = Account("A003", 2000.0)

# Add the accounts to the database
database.add_account(account1)
database.add_account(account2)
database.add_account(account3)

# Create a customer
customer = Customer("John Doe", "123 Main St", [account1, account2])

# Create a bank employee
employee = BankEmployee("Jane Smith", "456 Elm St", "Manager")

# Create a bank
bank = Bank("My Bank", [customer], [employee], database)

# Connect the bank employee to the customer
customer.accounts.append(account3)
# Test the functionality
print(bank.name)  # Output: My Bank
print()
print()

# Print customer details
print("Customers:\n")
for customer in bank._customers:
    print(customer)

# Print employee details
print("\n\nEmployees:\n")
for employee in bank._employees:
    print(employee)

print("\n\nDo you have access to this customer?")
print(bank._database.check_account(account1))  # Output: True

# Access customer's accounts
print("\n\nCustomer Accounts:\n")
for customer in bank._customers:
    for account in customer.accounts:
        print("Account Number:", account.account_number)
        print("Balance:", account.balance, "\n")