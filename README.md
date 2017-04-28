* needed:
    * 安装virtualenv
    * 激活环境 venv\Scripts\active
    * 安装flask   pip install flask
    * 安装包:
        * pip install blueprint
        * pip install flask-httpauth
        * pip install flask-script
        * pip install flask-json
        * pip install flask-cors
        * pip install flask-sqlalchemy
        * pip install flask-migrate
            * python hello.py db init
            * python hello.py db migrate -m "initial migration"
            * python hello.py db upgrade

     * 生成 requirements.txt
        * pip freeze > requirements.txt
     * 安装 requirements.txt 中的包
        * pip install -r requirements.txt


