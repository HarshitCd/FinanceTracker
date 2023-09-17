class Transaction:
    def __init__(self) -> None:
        self.date: str = input("Enter Date Of Transaction: ")
        self.credit_acc: str = input("Credit Account Name: ")
        self.debit_acc: str = input("Debit Account Name: ")
        self.amt: float = float(input("Enter The Amount Transacted: "))

    def get_data(self) -> dict:
        return {
            "date": self.date,
            "amount": self.amt,
            "credit_account_name": self.credit_acc,
            "debit_account_name": self.debit_acc,
        }