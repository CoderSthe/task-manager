def view_all():
    with open('tasks.txt', 'r') as f:
            for line in f:
                print(f"Task             :   {line.split(', ')[1]}")
                print(f"Assigned to      :   {line.split(', ')[0]}")
                print(f"Date Assigned    :   {line.split(', ')[3]}")
                print(f"Due Date         :   {line.split(', ')[4]}")
                print(f"Task Completed   :   {line.split(', ')[5]}")
                print(f"Task Description :   {line.split(', ')[2]}")
                print('\n')


def view_mine():
    username = input("Enter your username: ")
    g = open('temp.txt', 'w+')
    with open('tasks.txt', 'r') as f:
        count = 1
        tasks = []
        for line in f:
            if line.startswith(username):
                print(f"Task             :   {line.split(', ')[1]}")
                print(f"Assigned to      :   {line.split(', ')[0]}")
                print(f"Date Assigned    :   {line.split(', ')[3]}")
                print(f"Due Date         :   {line.split(', ')[4]}")
                print(f"Task Completed   :   {line.split(', ')[5]}")
                print(f"Task Description :   {line.split(', ')[2]}")
                print('\n')
            tasks.append(line)
            count += 1
            g.write(str(tasks))