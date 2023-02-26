import typer
from enum import Enum
from datetime import date, timedelta
from add_task import add_task
from authenticate_user import authenticate_user, valid_credentials
from view_tasks import view_all, view_mine
from gen_reports import generate_reports
from disp_stats import display_stats

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
    add_task()

@app.command()
def view(choice: ViewChoice):
    '''
    :   view assigned tasks
    '''
    if choice.value == 'all':
        view_all()
    elif choice.value == 'mine':
        view_mine()


@app.command()
def reports():
    '''
    :   generate reports
    '''
    generate_reports()


@app.command()
def stats():
    '''
    :   display task statistics
    '''
    display_stats()

if __name__ == '__main__':
    app()