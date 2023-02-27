from datetime import date, timedelta
def add_task():
    with open('current_user.txt', 'r') as f:
        username = f.read()
    task_complete = "No"
    task_title = input("Please enter the name of the task: ").title()
    task_descrip = input("Please enter a description of the task:\n").lower()
    task_assigned = date.today()
    task_due = task_assigned + timedelta(days=2)

    new_task = (f"{username}, {task_title}, {task_descrip}, {str(task_assigned)}, {str(task_due)}, {task_complete}")

    with open('tasks.txt', 'a') as g:
        g.write(f"{new_task}\n")
    print("\nNew task successfully added!\n")