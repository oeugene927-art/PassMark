"""Logging utility for bank management system"""

import logging
from datetime import datetime
import os


class BankLogger:
    """Logger for bank operations"""

    def __init__(self, log_file="bank_logs.txt"):
        """Initialize logger"""
        self.log_file = log_file
        self.setup_logger()

    def setup_logger(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def log_transaction(self, account_number, transaction_type, amount, balance):
        """Log a transaction"""
        message = f"Account {account_number}: {transaction_type} of ${amount:.2f}, New Balance: ${balance:.2f}"
        self.logger.info(message)

    def log_login(self, account_number):
        """Log user login"""
        self.logger.info(f"Login: Account {account_number}")

    def log_logout(self, account_number):
        """Log user logout"""
        self.logger.info(f"Logout: Account {account_number}")

    def log_error(self, message):
        """Log error message"""
        self.logger.error(message)
