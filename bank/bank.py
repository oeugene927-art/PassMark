"""Bank class for managing customers and accounts"""

from bank.customer import Customer


class Bank:
    """Represents a bank with multiple customers"""

    def __init__(self, bank_name="PassMark Bank"):
        """Initialize bank"""
        self.bank_name = bank_name
        self.customers = {}  # Dictionary with account_number as key
        self.accounts = {}

    def create_customer(self, name, email, phone, password, account_type="Checking"):
        """Create a new customer account"""
        customer = Customer(name, email, phone, password, account_type)
        self.customers[customer.account_number] = customer
        return customer

    def authenticate_customer(self, account_number, password):
        """Authenticate customer login"""
        customer = self.customers.get(account_number)
        if customer and customer.verify_password(password):
            return customer
        return None

    def get_customer(self, account_number):
        """Get customer by account number"""
        return self.customers.get(account_number)

    def transfer_funds(self, from_account, to_account, amount):
        """Transfer funds between accounts"""
        sender = self.customers.get(from_account)
        recipient = self.customers.get(to_account)

        if not sender or not recipient:
            return False

        if sender.withdraw(amount):
            recipient.deposit(amount)
            print(f"[Bank Log] Transfer: {from_account} → {to_account} (${amount:.2f})")
            return True
        return False

    def get_total_deposits(self):
        """Calculate total deposits across all accounts"""
        return sum(customer.get_balance() for customer in self.customers.values())

    def get_customer_count(self):
        """Get total number of customers"""
        return len(self.customers)

    def list_all_customers(self):
        """List all customers"""
        return list(self.customers.values())

    def __repr__(self):
        return f"Bank({self.bank_name}, Customers: {self.get_customer_count()}, Total Deposits: ${self.get_total_deposits():.2f})"
