import hashlib
def register_user():
    email = input("Enter email address: ")
    password = input("Enter password: ")
    confirmation = input("Confirm password: ")

    if confirmation == password:
        enc = confirmation.encode()
        hash1 = hashlib.sha256(enc).hexdigest()

        with open("credentials.txt", "a") as f:
            f.write(f"{email}\n")
            f.write(f"{hash1}\n")
        print("You have successfully been registered!")
    else:
        print("Password and password confirmation do not match.\n")