from os import read
import mConnection
from mConnection import cursor
from prettytable import PrettyTable


class login:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def set_role(self):
        read = '''
        SELECT role_id FROM `users` WHERE username = %s && password = %s
        '''
        val =(self.username, self.password)
        cursor.execute(read, val)
        for data in cursor.fetchall():
            self.role = data[0]
    
    def get_role(self):
        return self.role
        
    @staticmethod
    def menu():
        pass
