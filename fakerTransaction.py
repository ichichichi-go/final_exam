from faker import Faker
import random

def generate_fake_transactions(num_entries):
    fake = Faker()
    transactions = []

    for _ in range(num_entries):
        # Unique transaction ID (using a combination of random string or number)
        transaction_id = f"TXN{random.randint(1000, 9999)}"

        # Random transaction date
        transaction_date = fake.date_this_year()

        # Random amount (e.g., between 10 and 5000)
        amount = round(random.uniform(10, 5000), 2)

        transactions.append({
            "transaction_id": transaction_id,
            "transaction_date": transaction_date,
            "amount": amount
        })

    return transactions

def print_transactions(transactions):
    for transaction in transactions:
        print(f"Transaction ID: {transaction['transaction_id']}")
        print(f"Transaction Date: {transaction['transaction_date']}")
        print(f"Amount: ${transaction['amount']}")
        print('-' * 40)  # Adds a separator between transactions

if __name__ == "__main__":
    num_entries = 10  # Number of fake transactions to generate
    transactions = generate_fake_transactions(num_entries)
    print_transactions(transactions)
