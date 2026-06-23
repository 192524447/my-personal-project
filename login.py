def login(username, password):
    if username == "admin" and password == "123":
        return "Login Successful"
    else:
        return "Invalid Credentials"

print(login("admin","123"))