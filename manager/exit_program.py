import os

def logout_session():
    os.remove('current_user.txt')
    print("You have successfully logged out.")