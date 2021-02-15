import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{username}:{password}@{host}/{db_name}'.format(
    username=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    host=os.getenv('MYSQL_HOST'),
    db_name=os.getenv('MYSQL_DATABASE'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)