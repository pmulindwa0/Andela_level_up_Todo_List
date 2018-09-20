accounts = {}

def add_account(name, password):
    accounts[password] = name
    print(accounts)

def login(name, password):
    if (password in accounts) and (accounts[password] == name):
        return True
    else:
        return False

add_account("peter", "password")
print(login("petero", "password"))