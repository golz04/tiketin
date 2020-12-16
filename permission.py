from connection import cursor
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

    def get_roles_data():
        read='SELECT * FROM user_roles'
        cursor.execute(read)
        print('id\tnama roles')
        for data in cursor.fetchall():
            print(*data, sep="\t")
    
    def get_chairs_data():
        read='SELECT * FROM chairs'
        cursor.execute(read)
        print('id\tnumber\tstatus')
        for data in cursor.fetchall():
            print(*data, sep="\t")


if __name__ == "__main__":
    permisi =permission(1,1,1,1)
    permission.get_chairs_data()
