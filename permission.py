from connection import cursor
from prettytable import PrettyTable
import connection


class permission:
    def __init__(self, permission_id, permission_role, permission_title, permission_description):
        self.permission_id = permission_id
        self.permission_role = permission_role
        self.permission_title = permission_title
        self.permission_description = permission_description

    def add_permission(self):
        pass

    def edit_permission(self):
        pass

    def delete_permission(self):
        pass

    def search_permission(self):
        pass

    def show_roles_data():
        read='SELECT * FROM user_roles'
        cursor.execute(read)
        table = PrettyTable(['id','nama roles'])
        table.add_rows(cursor.fetchall())
        print(table)
    
    def show_chairs_data():
        read='SELECT * FROM chairs'
        cursor.execute(read)
        table = PrettyTable(['id','number','status'])
        table.add_rows(cursor.fetchall())
        print(table)

    def show_companies_data():
        read='SELECT * FROM companies'
        cursor.execute(read)
        table = PrettyTable(['id','company name','address'])
        table.add_rows(cursor.fetchall())
        print(table)
            
    def show_genres_data():
        read='SELECT * FROM genres'
        cursor.execute(read)
        table = PrettyTable(['id','genre name'])
        table.add_rows(cursor.fetchall())
        print(table)

    def show_movies_data():
        read='SELECT * FROM movies'
        cursor.execute(read)
        table = PrettyTable(['id', 'title', 'genre', 'company'])
        table.add_rows(cursor.fetchall())
        print(table)
            
    def show_schedules_data():
        read='SELECT * FROM schedules'
        cursor.execute(read)
        table= PrettyTable(['id', 'date', 'start', 'ends', 'movie', 'studio'])
        table.add_rows(cursor.fetchall())
        print(table)

    def show_studio_data():
        read='SELECT * FROM studios'
        cursor.execute(read)
        table= PrettyTable(['id', 'studio', 'description'])
        table.add_rows(cursor.fetchall())
        print(table)
    
if __name__ == "__main__":
    permisi =permission(1,1,1,1)
    permission.show_studio_data()
