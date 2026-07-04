"""Account class for managing different account types"""

from datetime import datetime


class Account:
    """Represents a bank account"""

    ACCOUNT_TYPES = ["Checking", "Savings", "Money Market"]
    INTEREST_RATES = {
        "Checking": 0.01,
        "Savings": 0.05,
        "Money Market": 0.08
    }

    def __init__(self, account_number, account_type="Checking"):
        """Initialize account"""
        if account_type not in self.ACCOUNT_TYPES:
            raise ValueError(f"Invalid account type. Choose from {self.ACCOUNT_TYPES}")
        
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0.0
        self.created_at = datetime.now()
        self.interest_rate = self.INTEREST_RATES[account_type]

    def calculate_interest(self, months=12):
        """Calculate interest earned on balance"""
        interest = self.balance * self.interest_rate * (months / 12)
        return interest

    def apply_interest(self):
        """Apply yearly interest to balance"""
        interest = self.calculate_interest()
        self.balance += interest
        return interest

    def __repr__(self):
        return f"Account({self.account_number}, {self.account_type}, Balance: ${self.balance:.2f})"
