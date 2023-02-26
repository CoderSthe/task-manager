import typer
from enum import Enum
from datetime import date, timedelta

from authenticate_user import authenticate_user, valid_credentials

app = typer.Typer()

class ViewChoice(Enum):
    view_all = 'all'
    view_mine = 'mine'


@app.command()
def login():
    '''
    :   authenticate user
    '''
    creds = valid_credentials()
    return authenticate_user(creds)


# @app.command()
# def register():
#     '''
#     :   register a new user
#     '''
#     pass


@app.command()
def add():
    '''
    :   add a new task
    '''
    task_complete = "No"
    task_user = input("Please enter the username who has been assigned the task: ")
    task_title = input("Please enter the name of the task: ")
    task_descrip = input("Please enter a description of the task:\n")
    task_assigned = date.today()
    task_due = task_assigned + timedelta(days=2)

    new_task = (f"\n {task_user}, {task_title}, {task_descrip}, {str(task_assigned)}, {str(task_due)}, {task_complete}")

    with open('tasks.txt', 'a') as g:
        g.write(new_task)
    print("\nNew task successfully added!\n")


def view(choice: ViewChoice):
    '''
    :   view assigned tasks
    '''
    if view.value == 'all':
        with open('tasks.txt', 'r') as f:
            for line in f:
                print(f"Task             :   {line.split(', ')[1]}")
                print(f"Assigned to      :   {line.split(', ')[0]}")
                print(f"Date Assigned    :   {line.split(', ')[3]}")
                print(f"Due Date         :   {line.split(', ')[4]}")
                print(f"Task Completed   :   {line.split(', ')[5]}")
                print(f"Task Description :   {line.split(', ')[2]}")
                print('\n')
    if view.value == 'mine':
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


@app.command()
def reports():
    '''
    :   generate reports
    '''
    pass


@app.command()
def stats():
    '''
    :   display task statistics
    '''
    pass

if __name__ == '__main__':
    app()
