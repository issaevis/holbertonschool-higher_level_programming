#!/usr/bin/python3

from file1 import *


class BankDatabase:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
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
        self._customers = list()
        self._employees = list()
        self._database = database

