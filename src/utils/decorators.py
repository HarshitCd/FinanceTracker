import toml

def write_all_to_db(func):
    def write_all(*args, **kwargs):
        curr_transactions, db_loc = func(*args, **kwargs)
        
        with open(db_loc, 'w') as toml_file:
            toml.dump(curr_transactions, toml_file)

    return write_all
