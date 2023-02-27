import hashlib
import getpass

def login_user():
    email = input("Enter email: ")
    password = getpass.getpass("Enter password: ")
    # password = input("Enter password: ")

    auth = password.encode()
    auth_hash = hashlib.sha256(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_password = f.read().split(", ")
        stored_password = stored_password.strip()
    
    if email == stored_email and auth_hash == stored_password:
        print("Logged in successfully!")
    else:
        print("Login failed!\n")