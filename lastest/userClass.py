from os import read
import connection
from connection import cursor
from prettytable import PrettyTable

def sql_execute(temporary):
    cursor.execute(temporary[0], temporary[1])
    connection.db.commit()
    print('esekusi sukses')


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

    def get_schedules_today(self):
        read = 'SELECT schedules.id_schedule, movies.title, schedules.date_schedule, schedules.start, schedules.end, studios.studio_name FROM schedules INNER JOIN movies ON schedules.film_code = movies.code_film INNER JOIN studios ON schedules.id_studio = studios.id_studio'
        cursor.execute(read)
        fetch = cursor.fetchall()
        for data in fetch:
            self.temporary_data.append(data)
        table = PrettyTable(['ID Jadwal', 'Nama Film', 'Tanggal Film', 'Mulai', 'Selesai', 'Studio'])
        table.add_rows(fetch)
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

    def get_topping_data(self):
        read='SELECT * FROM toppings'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table= PrettyTable(['id', 'nama topping', 'harga'])
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

    @staticmethod
    def menu():
        print('\t\t'+'='*8+'input data'+'='*8)
        print('\t\t1. add user')
        print('\t\t2. add movie')
        print('\t\t3. add schedule')
        print('\t\t4. add topping')
        print('\t\t'+'='*8+'hapus data'+'='*8)
        print('\t\t5. hapus user')
        print('\t\t6. hapus movie')
        print('\t\t7. hapus schedule')
        print('\t\t8. hapus topping')
        n = int(input('masukan pilihan : '))
        return n
    
    @staticmethod
    def add_user():
        ulang = True
        #memasukan nama
        name = input('masukan nama : ')
        #memasukan email
        username = input('masukan username : ')
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

        sql = 'INSERT INTO users (id_user, name, username, password, gender, contact, address, role_id) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)'
        val = (name, username, password, gender, contact, alamat, role_id)
        sqlQuery = (sql, val)
        return  sqlQuery

    @staticmethod
    def add_schedule(movie_data, studio_data):
        tanggal = int(input('masukan tanggal (numerik): '))
        bulan = int(input('masukan bulan (numerik): '))
        tahun = int(input('masukan tanggal (numerik): '))
        date = '{}-{}-{}'.format(tahun, bulan, tanggal)
        startInput = input('masukan jam film mulai(jam:menit) : ')
        start = '{}:00'.format(startInput)
        endInput = input('masukan jam film selesai(jam:menit) : ')
        end = '{}:00'.format(endInput)
        print(movie_data)
        film = int(input('masukan id film : '))
        print(studio_data)
        studio = int(input('masukan id studio : '))
        sql = 'INSERT INTO schedules (id_schedule, date_schedule, start, end, film_code, id_studio) VALUES (NULL, %s, %s, %s, %s, %s)'
        val = (date, start, end, film, studio)
        sqlQuery = (sql, val)
        return sqlQuery

    @staticmethod
    def add_movie(genre_data, company_data):
        judul = input('masukan judul film : ')
        print(genre_data)
        genre = int(input('masukan id genre : '))
        print(company_data)
        company = int(input('masukan id company : '))
        sql = 'INSERT INTO movies (code_film, title, genre_id, company_id) VALUES (NULL, %s, %s, %s)'
        val = (judul, genre, company)
        sqlQuery = (sql, val)
        return sqlQuery
    
    @staticmethod
    def add_topping():
        topping = input('masukan nama snack/minuman : ')
        harga = int(input('masukan harga : '))
        sql = 'INSERT INTO toppings (id_topping, topping_name, price) VALUES (NULL, %s, %s)'
        val = (topping, harga)
        sqlQuery = (sql, val)
        return sqlQuery

    @staticmethod
    def delete_movie(movie_data):
        print(movie_data)
        n = int(input('masukan id yang ingin dihapus : '))
        sql = 'DELETE FROM movies WHERE code_film = %s'
        val = (n,)
        sqlQuery = (sql, val)
        return sqlQuery
    
    @staticmethod
    def delete_schedule(schedule_data):
        print(schedule_data)
        n = int(input('masukan id yang ingin dihapus : '))
        sql = 'DELETE FROM schedules WHERE id_schedule = %s'
        val = (n,)
        sqlQuery = (sql, val)
        return sqlQuery

    @staticmethod
    def delete_user(user_data):
        print(user_data)
        n = int(input('masukan id yang ingin dihapus : '))
        sql = 'DELETE FROM users WHERE id_user = %s'
        val = (n,)
        sqlQuery = (sql, val)
        return sqlQuery

    @staticmethod
    def delete_topping(topping_data):
        print(topping_data)
        n = int(input('masukan id yang ingin dihapus : '))
        sql = '''DELETE FROM toppings WHERE id_topping = %s'''
        val = (n,)
        sqlQuery = (sql, val)
        return sqlQuery


class user(login):
    def __init__(self, username, password, role):
        super().__init__(username, password, role)

    @staticmethod
    def menu():
        print('\t\t'+'='*8+'input data'+'='*8)
        print('\t\t1. See schedule movie')
        n = int(input('masukan pilihan : '))
        return n
        
if __name__ == "__main__":
    permisi = permission(1)
    print(permisi.get_schedules_today())