def factoial(x):
    for i in range(1, x):
        x *= i
    return x

def autentification(**kwargs):
    users = {"admin":"admin", 
             "Azamat":"12345", 
             "John":"qwerty"}
    login = kwargs.get("login")
    password = kwargs.get("password")

    if login in users and users[login] == password:
        return f"Welcome {login}!"
    else:
        return "Invalid login or password"
    

