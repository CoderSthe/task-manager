from datetime import date, timedelta
def add_task():
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