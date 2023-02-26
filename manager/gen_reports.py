
import sys
def generate_reports():
    with open('current_cred.txt', 'r') as f:
        username = f.read()
    if username != "admin":
        print("This is an invalid option.\n")
        sys.exit()
    else:
        to = open('task_overview.txt', 'w')
        uo = open('user_overview.txt', 'w')
        f1 = open('tasks.txt', 'r')
        f2 = open('manager/user.txt', 'r')

        task_count = 0
        user_count = 0

        for i in f1:
            task_count += 1

        to.write("Total number of tasks generated:\t" + str(task_count) + '\n')
        print("task_overview.txt report succcessfully generated.")

        for i in f2:
            user_count += 1

        uo.write("Total number of users registered:\t" + str(user_count) + '\n')
        uo.write("Total number of tasks generated:\t" + str(task_count) + '\n')


        print("useroverview.txt report successfully generated.")

        to.close()
        uo.close()
        f1.close()
        f2.close()