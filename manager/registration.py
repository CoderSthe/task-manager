import hashlib
def register_user():
    email = input("Enter email address: ")
    password = input("Enter password: ")
    confirmation = input("Confirm password: ")

    if confirmation == password:
        enc = confirmation.encode()
        hash1 = hashlib.md5(enc).hexdigest()

        with open("credentials.txt", "w") as f:
            f.write(f"{email}\n")
            f.write(hash1)
        print("You have successfully been registered!")
    else:
        print("Password and password confirmation do not match.\n")