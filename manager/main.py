import typer
from enum import Enum
from datetime import date, timedelta
from add_task import add_task
from view_tasks import view_all, view_mine
from gen_reports import generate_reports
from disp_stats import display_stats
from registration import register_user
from login import login_user
from exit_program import logout_session

app = typer.Typer()

class ViewChoice(Enum):
    view_all = 'all'
    view_mine = 'mine'


@app.command()
def login():
    '''
    :   authenticate user
    '''
    login_user()


@app.command()
def register():
    '''
    :   register a new user
    '''
    typer.echo('registering new user...')
    register_user()


@app.command()
def add():
    '''
    :   add a new task
    '''
    typer.echo('adding new task...')
    add_task()

@app.command()
def view(choice: ViewChoice):
    '''
    :   view assigned tasks
    '''
    if choice.value == 'all':
        typer.echo('viewing all tasks...')
        view_all()
    elif choice.value == 'mine':
        typer.echo('viewing tasks assigned to you...')
        view_mine()


@app.command()
def reports():
    '''
    :   generate reports
    '''
    typer.echo('generating reports...')
    generate_reports()


@app.command()
def stats():
    '''
    :   display task statistics
    '''
    typer.echo('displaying stats...')
    display_stats()


@app.command()
def logout():
    '''
    :   log out of current session
    '''
    logout_session()

if __name__ == '__main__':
    app()
