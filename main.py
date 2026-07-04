#!/usr/bin/env python3
"""
Bank Management System - Main Entry Point
"""

from bank.bank import Bank
from bank.customer import Customer
from utils.validation import validate_amount, validate_account_number
import getpass
from datetime import datetime


def main():
    """Main application loop"""
    bank = Bank()
    current_user = None

    print("\n" + "="*50)
    print("Welcome to PassMark Bank Management System")
    print("="*50 + "\n")

    while True:
        if current_user is None:
            print("\n--- Main Menu ---")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("\nSelect an option (1-3): ").strip()

            if choice == "1":
                create_account(bank)
            elif choice == "2":
                current_user = login(bank)
            elif choice == "3":
                print("\nThank you for using PassMark Bank. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        else:
            print(f"\n--- Welcome {current_user.name} ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. View Transaction History")
            print("6. Account Details")
            print("7. Logout")
            choice = input("\nSelect an option (1-7): ").strip()

            if choice == "1":
                check_balance(current_user)
            elif choice == "2":
                deposit(current_user)
            elif choice == "3":
                withdraw(current_user)
            elif choice == "4":
                transfer(bank, current_user)
            elif choice == "5":
                view_history(current_user)
            elif choice == "6":
                view_details(current_user)
            elif choice == "7":
                print(f"\nLogging out {current_user.name}...")
                current_user = None
            else:
                print("Invalid option. Please try again.")


def create_account(bank):
    """Create a new customer account"""
    print("\n--- Create Account ---")
    name = input("Enter your full name: ").strip()
    
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your full name: ").strip()
    
    email = input("Enter your email address: ").strip()
    phone = input("Enter your phone number: ").strip()
    password = getpass.getpass("Set your password: ")
    
    try:
        customer = bank.create_customer(name, email, phone, password)
        print(f"\n✓ Account created successfully!")
        print(f"Account Number: {customer.account_number}")
        print(f"Name: {customer.name}")
    except Exception as e:
        print(f"✗ Error creating account: {e}")


def login(bank):
    """Login to an existing account"""
    print("\n--- Login ---")
    account_num = input("Enter your account number: ").strip()
    password = getpass.getpass("Enter your password: ")
    
    try:
        customer = bank.authenticate_customer(account_num, password)
        if customer:
            print(f"\n✓ Login successful! Welcome {customer.name}")
            return customer
        else:
            print("✗ Invalid account number or password.")
            return None
    except Exception as e:
        print(f"✗ Login error: {e}")
        return None


def check_balance(customer):
    """Check account balance"""
    balance = customer.get_balance()
    print(f"\n--- Account Balance ---")
    print(f"Account Number: {customer.account_number}")
    print(f"Balance: ${balance:.2f}")


def deposit(customer):
    """Deposit money into account"""
    print("\n--- Deposit Money ---")
    try:
        amount = float(input("Enter amount to deposit: $"))
        if validate_amount(amount):
            customer.deposit(amount)
            print(f"\n✓ Successfully deposited ${amount:.2f}")
            print(f"New Balance: ${customer.get_balance():.2f}")
        else:
            print("✗ Invalid amount. Please enter a positive number.")
    except ValueError:
        print("✗ Invalid input. Please enter a valid amount.")


def withdraw(customer):
    """Withdraw money from account"""
    print("\n--- Withdraw Money ---")
    print(f"Current Balance: ${customer.get_balance():.2f}")
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if validate_amount(amount):
            if customer.withdraw(amount):
                print(f"\n✓ Successfully withdrew ${amount:.2f}")
                print(f"New Balance: ${customer.get_balance():.2f}")
            else:
                print("✗ Insufficient balance for withdrawal.")
        else:
            print("✗ Invalid amount. Please enter a positive number.")
    except ValueError:
        print("✗ Invalid input. Please enter a valid amount.")


def transfer(bank, customer):
    """Transfer money to another account"""
    print("\n--- Transfer Money ---")
    print(f"Your Current Balance: ${customer.get_balance():.2f}")
    
    recipient_account = input("Enter recipient's account number: ").strip()
    
    if not validate_account_number(recipient_account):
        print("✗ Invalid account number format.")
        return
    
    try:
        amount = float(input("Enter amount to transfer: $"))
        if validate_amount(amount):
            if bank.transfer_funds(customer.account_number, recipient_account, amount):
                print(f"\n✓ Successfully transferred ${amount:.2f}")
                print(f"Recipient Account: {recipient_account}")
                print(f"Your New Balance: ${customer.get_balance():.2f}")
            else:
                print("✗ Transfer failed. Please check the recipient account number.")
        else:
            print("✗ Invalid amount. Please enter a positive number.")
    except ValueError:
        print("✗ Invalid input. Please enter a valid amount.")


def view_history(customer):
    """View transaction history"""
    print("\n--- Transaction History ---")
    history = customer.get_transaction_history()
    
    if not history:
        print("No transactions found.")
        return
    
    print(f"\n{'Date':<20} {'Type':<12} {'Amount':<12} {'Balance':<12}")
    print("-" * 56)
    for transaction in history:
        print(transaction)


def view_details(customer):
    """View account details"""
    print("\n--- Account Details ---")
    print(f"Name: {customer.name}")
    print(f"Account Number: {customer.account_number}")
    print(f"Email: {customer.email}")
    print(f"Phone: {customer.phone}")
    print(f"Account Type: {customer.account_type}")
    print(f"Balance: ${customer.get_balance():.2f}")
    print(f"Account Created: {customer.created_at}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
