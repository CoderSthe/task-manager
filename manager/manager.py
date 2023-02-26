import typer
from enum import Enum

app = typer.Typer()

class ViewChoice(Enum):
    view_all = 'all'
    view_mine = 'mine'


@app.command()
def login():
    '''
    :   authenticate user
    '''
    pass


@app.command()
def register():
    '''
    :   register a new user
    '''
    pass


@app.command()
def add():
    '''
    :   add a new task
    '''
    pass


def view(choice: ViewChoice):
    '''
    :   view assigned tasks
    '''
    if view.value == 'all':
        pass
    if view.value == 'mine':
        pass


@app.command()
def reports():
    '''
    :   generate reports
    '''
    pass


@app.command()
def stats():
    '''
    display task statistics
    '''
    pass

if __name__ == '__main__':
    app()
