import uuid

from models.transactions import Transaction
from tabulate import tabulate
from utils.decorators import write_all_to_db

@write_all_to_db
def post(transactions: dict, db_loc: str):
    transaction = Transaction()
    transactions[str(uuid.uuid4())] = transaction.get_data()

    return transactions, db_loc

@write_all_to_db
def put(transactions: dict, transaction_id: str, db_loc: str):
    transaction = Transaction()
    transactions[transaction_id] = transaction.get_data()

    return transactions, db_loc

@write_all_to_db
def delete(transactions: dict, transaction_id: str, db_loc: str):
    transactions.pop(transaction_id, None)
    
    return transactions, db_loc

def display_transactions(transactions: dict):
    table_data = [
        {
            "date": val.get("date"), 
            "credit account": val.get("credit_account_name"),
            "debit account": val.get("debit_account_name"), 
            "amount": val.get("amount")
        }
        for val in transactions.values()
    ]
    print(tabulate(table_data, headers="keys", tablefmt="pretty"))
