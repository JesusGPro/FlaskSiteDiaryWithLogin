from flask import current_app
from flask_login import UserMixin

"""
For handling login management, we'll use the Flask-login plugin. This plugin requires us to implement a class
for representing users on our site. Our user data basically consists of a username and a password. Flask-login
assumes that there will be a aunique string value for identifying each user. In most cases, this will be the 
string value of the database id number for a user. In our example, we will use the username for this purpose.
Flask-login also keeps an attribute for checking whether a user is active or not(self.active = True). And we
add an attribute for marking users with administrative privileges (self.is_amin = False)
"""

class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.active = True
        self.is_admin = False

    def get_id(self):
        return self.username

    @property
    def is_active(self):
        return self.active


def get_user(user_id):
    password = current_app.config["PASSWORDS"].get(user_id)
    user = User(user_id, password) if password else None
    if user is not None:
        user.is_admin = user.username in current_app.config["ADMIN_USERS"]
    return user


"""Given a user's id, returns the user object associated with that id (def get_user(user_id)), first checks whether 
there is an entry in the passwords map, and if so, creates the user object (passord and user). Also sets the is_admin
property according to the user being in the ADMIN_USERS settings or not.
"""