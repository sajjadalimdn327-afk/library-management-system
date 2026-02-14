# admin.py
# This file handles admin login

class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "123"

    def login(self, user, pwd):
        if user == self.username and pwd == self.password:
            return True
        else:
            return False
