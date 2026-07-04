"""Transaction class for recording bank transactions"""

from datetime import datetime


class Transaction:
    """Represents a single transaction"""

    def __init__(self, transaction_type, amount, balance_after):
        """Initialize transaction"""
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()

    def __str__(self):
        """Return formatted transaction string"""
        date_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"{date_str:<20} {self.transaction_type:<12} ${self.amount:<11.2f} ${self.balance_after:<11.2f}"

    def __repr__(self):
        return f"Transaction({self.transaction_type}, ${self.amount}, Balance: ${self.balance_after})"
