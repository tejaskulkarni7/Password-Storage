from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

myapp_obj = Flask(__name__) #flask object
db = SQLAlchemy(myapp_obj)  #database object
bcrypt = Bcrypt(myapp_obj)  #flask library to hash passwords instead of storing them as it is
login_manager = LoginManager(myapp_obj) #for login
login_manager.login_view = "loginPage"  #for login
login_manager.login_message_category = "info" #for login


myapp_obj.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cs166.db' #SQLlite configuration
myapp_obj.config['SECRET_KEY'] = 'abc'      #DO NOT CHANGE THIS HEXADECIMAL SECRET_KEY

from app import routes


#RUN ONCE AND THEN COMMENT FOLLOWING CODE:
#db.drop_all()
#db.create_all()
