#!~/CodeNew/jixie-backend/venv python
from flask_script import Manager, Shell
from app import create_app

app = create_app()
manager = Manager(app)
# manager.add_command("shell", Shell(make_context=make_shell_context))

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
