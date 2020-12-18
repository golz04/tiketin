import connection
from connection import cursor
from prettytable import PrettyTable

class permission:
    access = False
    temporary_data =[]
    def __init__(self, role_id):
        self.role_id = role_id

    def set_role_id(self, role_id):
        self.role_id = role_id

    def set_permission(self):
        if self.role_id == 1:
            self.access = True
        if self.role_id ==2:
            self.access = False
    
    def get_permission(self):
        return self.access

    def add_permission(self):
        pass

    def edit_permission(self):
        pass

    def delete_permission(self):
        pass

    def search_permission(self):
        pass

    def get_users_data(self):
        read='SELECT * FROM users'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table = PrettyTable(['id','name', 'username', 'password', ' gender', ' contact', 'address', 'role id'])
        table.add_rows(a)
        return table        

    def get_roles_data(self):
        read='SELECT * FROM user_roles'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table = PrettyTable(['id','nama roles'])
        table.add_rows(a)
        return table
    
    def get_chairs_data(self):
        read='SELECT * FROM chairs'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table = PrettyTable(['id','number','status'])
        table.add_rows(a)
        return table

    def get_companies_data(self):
        read='SELECT * FROM companies'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table = PrettyTable(['id','company name','address'])
        table.add_rows(a)
        return table
            
    def get_genres_data(self):
        read='SELECT * FROM genres'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table = PrettyTable(['id','genre name'])
        table.add_rows(a)
        return table

    def get_movies_data(self):
        read='SELECT * FROM movies'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table = PrettyTable(['id', 'title', 'genre', 'company'])
        table.add_rows(a)
        return table
            
    def get_schedules_data(self):
        read='SELECT * FROM schedules'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table= PrettyTable(['id', 'date', 'start', 'ends', 'movie', 'studio'])
        table.add_rows(a)
        return table

    def get_studio_data(self):
        read='SELECT * FROM studios'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table= PrettyTable(['id', 'studio', 'description'])
        table.add_rows(a)
        return table

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

class admin(login):
    def __init__(self, username, password, role):
        super().__init__(username, password, role)
    
    def add_user(self):
        ulang = True
        #memasukan nama
        name = input('masukan nama : ')
        #memasukan email
        email = input('masukan email : ')
        #memasukan password
        while ulang == True:
            password = input('masukan password : ')
            password_confirm = input('masukan password sekali lagi : ')
            if password == password_confirm:
                ulang = False
        ulang = True
        #memasukan gender
        while ulang == True:
            gender = input('masukan gender (L/P) : ').upper()
            if gender == 'L' or gender =='P':
                ulang = False
            else:
                print('masukan sesuai format')
        #memasukan kontak
        contact = input('masukan kontak : ')
        #memasukan alamat
        alamat = input('masukan alamat : ')
        #masukan role
        read='SELECT * FROM user_roles'
        cursor.execute(read)
        print('id\tnama roles')
        for data in cursor.fetchall():
            print('{}\t{}'.format(data[0], data[1]))
        role_id = int(input('masukan role id : '))

        sql = 'INSERT INTO users (id_user, name, email, password, gender, contact, address, role_id) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)'
        val = (name, email, password, gender, contact, alamat, role_id)
        sqlQuery = [sql, val]
        return  sqlQuery


    def add_schedule(self):
        pass

    def add_movie(self):
        pass

    def delete_movie(self):
        pass

    def delete_schedule(self):
        pass

    def add_topping(self):
        pass
    
    def sql_execute(self, temporary):
        try:
            cursor.execute(temporary[0], temporary[1])
            connection.db.commit()
            print('input sukses')
        except:
            print('error gan')

if __name__ == "__main__":
    permisi = permission(0)
    print(permisi.get_users_data())
    print(permisi.temporary_data)