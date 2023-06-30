#!/usr/bin/python3
'''Module to create a class'''


import json


class Person:
    '''class person that defines a person'''
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
    
    def __str__(self):
        return "Name: {} - Address: {}".format(self.name, self.address)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, string):
        if not string:
            raise ValueError("Name cannot be empty")
        else:
            self.__name = string

    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, string):
        if not string:
            raise ValueError("Address cannot be empty")
        else:
            self.__address = string


class Customer(Person):
    '''class that represents a customer'''
    def __init__(self, name, address, accounts):
        super().__init__(name, address)
        self.__accounts = accounts

    @property
    def accounts(self):
        return self.__accounts
    
    @accounts.setter
    def accounts(self, listofaccount):
        if not isinstance(listofaccount, list):
            raise TypeError('Accounts should be an instance of List')
        else:
            self.__accounts = listofaccount

    def __str__(self):
        return f"Customer - Name: {self.name} - Address: {self.address}"


class BankEmployee(Person):
    '''Class that represents a bank employee'''
    employee_id = 0

    def __init__(self, name, address, position):
        super().__init__(name, address)
        self.__position = position
        BankEmployee.employee_id += 1

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, string):
        if not isinstance(string, str):
            raise TypeError('Position must be a String')
        else:
            self.__position = string

    def __str__(self):
        return f"Bank Employee - Name: {self.name} - Address: {self.address} - Position: {self.position}"

class Account:
    '''class that specifies an account'''
    def __init__(self, account_number, balance):
        self.__account_number = account_number 
        self.__balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @account_number.setter
    def account_number(self, number):
        if not isinstance(number, (str, int)):
            raise TypeError('Account Number Must Be A String Or Integer')
        else:
            self.__account_number = number

    @balance.setter
    def balance(self, floatn):
        if not isinstance(floatn, float):
            raise TypeError('Balance Must Be Float Type')
        else:
            self.__balance = floatn

class SavingsAccount(Account):
    '''subclass from account that specifies a savings account'''
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if not isinstance(value, float):
            raise ValueError("Interest Rate must be a floating point")
        else:
            self.__interest_rate = value


class BankDatabase:
    def __init__(self):
        self.__accounts = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.__accounts.append(account)
        else:
            raise TypeError('Account must be an instance of Account')

    def remove_account(self, account):
        if isinstance(account, Account):
            if account in self.__accounts:
                self.__accounts.remove(account)
            else:
                raise ValueError('Account not found in the database')
        else:
            raise TypeError('Account must be an instance of Account')

    def check_account(self, account):
        if isinstance(account, Account):
            return True if (account in self.__accounts) else False

    def sort_accounts(self, criterion):
        if criterion == 'balance':
            self.__accounts.sort(key=lambda account: account.balance)
        elif criterion == 'account_number':
            self.__accounts.sort(key=lambda account: account.account_number)
        else:
            raise ValueError('Invalid sorting criterion')

        
class Bank:
    """A class that represents a bank"""
    def __init__(self, name, customers, employees, database):
        self.name = name
        self._customers = customers
        self._employees = employees
        self._database = database

