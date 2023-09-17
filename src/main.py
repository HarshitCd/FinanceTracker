import toml

import utils.utils as ut

def main() -> None:
    config: dict = toml.load("src/configs/config.toml")
    db_loc = config.get("transactions", {}).get("loc", "")
    transactions: dict  = toml.load(db_loc)
    
    ut.display_transactions(transactions=transactions)

if __name__ == '__main__':
    main()