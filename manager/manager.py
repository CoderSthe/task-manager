import typer
from enum import Enum
from datetime import date, timedelta
from add_task import add_task
from authenticate_user import authenticate_user, valid_credentials
from view_tasks import view_all, view_mine

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


def view(choice: ViewChoice):
    '''
    :   view assigned tasks
    '''
    if view.value == 'all':
        view_all()
    elif view.value == 'mine':
        view_mine()


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
