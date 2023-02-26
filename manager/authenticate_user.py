def authenticate_user(credentials):
    attempts_left = 3
    while attempts_left > 0:
        username = input('Please enter your username: ')
        password = input('Please enter your password: ')
        if not credentials.get(username) or password != credentials[username]:
             print('Your username or password is incorrect. \n')
             attempts_left -= 1
             continue
        if credentials.get(username) and password == credentials[username]:
            return True
    print('You have made 3 incorrect attempts. Please try again later.')
    return False



def valid_credentials():
    lst_username = []
    lst_password = []
    with open('manager/user.txt', 'r+') as f:
        for line in f:
            valid_username, valid_password = line.split(', ')
            valid_password = valid_password.strip()
            lst_username.append(valid_username)
            lst_password.append(valid_password)

    return dict(zip(lst_username, lst_password))

if __name__ == '__main__':
    creds = valid_credentials()
    authenticate_user(creds)
