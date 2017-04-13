#!~/CodeNew/jixie-backend/venv python
from flask_script import Manager, Shell
from app import create_app, db
from app.models import Material
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, Material=Material)
manager.add_command("shell", Shell(make_context=make_shell_context))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
