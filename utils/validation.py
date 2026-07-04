"""Validation utility functions"""

import re


def validate_amount(amount):
    """Validate if amount is positive number"""
    try:
        amount = float(amount)
        return amount > 0
    except (ValueError, TypeError):
        return False


def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_phone(phone):
    """Validate phone number format"""
    # Remove common separators
    cleaned = re.sub(r'[\s\-().]', '', phone)
    # Check if it's 10 digits
    return cleaned.isdigit() and len(cleaned) >= 10


def validate_account_number(account_number):
    """Validate account number format (10 digits)"""
    return account_number.isdigit() and len(account_number) == 10


def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit
