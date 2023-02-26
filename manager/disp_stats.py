import sys
def display_stats():
    with open('current_cred.txt', 'r') as f:
        username = f.read()
    if username != "admin":
        print("You have selected an invalid option. Please try again\n")
        sys.exit()
    else:
        f = open('manager/user.txt', 'r')
        g = open('tasks.txt', 'r')

        num_users = 0
        num_tasks = 0

        for line in f:
            num_users += 1

        for line in g:
            num_tasks += 1

        print(f"Number of users             :   {num_users}")
        print(f"Number of tasks             :   {num_tasks}")

        # close the files
            
        f.close()
        g.close()