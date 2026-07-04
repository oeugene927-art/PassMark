"""Customer class for bank management system"""

import hashlib
from datetime import datetime
from bank.transaction import Transaction
import random
import string


class Customer:
    """Represents a bank customer"""

    def __init__(self, name, email, phone, password, account_type="Checking"):
        """Initialize a new customer"""
        self.name = name
        self.email = email
        self.phone = phone
        self.account_type = account_type
        self.balance = 0.0
        self.password_hash = self._hash_password(password)
        self.created_at = datetime.now()
        self.account_number = self._generate_account_number()
        self.transactions = []

    @staticmethod
    def _hash_password(password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def _generate_account_number():
        """Generate a unique account number"""
        return ''.join(random.choices(string.digits, k=10))

    def verify_password(self, password):
        """Verify if provided password matches stored hash"""
        return self.password_hash == self._hash_password(password)

    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.balance += amount
            transaction = Transaction("Deposit", amount, self.balance)
            self.transactions.append(transaction)
            return True
        return False

    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            transaction = Transaction("Withdrawal", amount, self.balance)
            self.transactions.append(transaction)
            return True
        return False

    def get_balance(self):
        """Get current account balance"""
        return self.balance

    def get_transaction_history(self, limit=None):
        """Get transaction history"""
        if limit:
            return self.transactions[-limit:]
        return self.transactions

    def __repr__(self):
        return f"Customer({self.name}, Account: {self.account_number}, Balance: ${self.balance:.2f})"
