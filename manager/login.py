import hashlib

def login_user():
    email = input("Enter email: ")
    password = input("Enter password: ")

    auth = password.encode()
    auth_hash = hashlib.sha256(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_password = f.read().split("\n")
    
    if email == stored_email and auth_hash == stored_password:
        print("Logged in successfully!")
    else:
        print("Login failed!\n")