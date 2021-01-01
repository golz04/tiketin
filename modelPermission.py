from os import read
import mConnection
from mConnection import cursor
from prettytable import PrettyTable
from datetime import date

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


    #user
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

    def get_topping_data(self):
        read='SELECT * FROM toppings'
        cursor.execute(read)
        a = cursor.fetchall()
        for data in a:
            self.temporary_data.append(data)
        table= PrettyTable(['id', 'nama topping', 'harga'])
        table.add_rows(a)
        return table


    # customer
    def get_schedules_all(self):
        read = 'SELECT schedules.id_schedule, movies.title, schedules.date_schedule, schedules.start, schedules.end, studios.studio_name FROM schedules INNER JOIN movies ON schedules.film_code = movies.code_film INNER JOIN studios ON schedules.id_studio = studios.id_studio'
        cursor.execute(read)
        fetch = cursor.fetchall()
        for data in fetch:
            self.temporary_data.append(data)
        table = PrettyTable(['ID Jadwal', 'Nama Film', 'Tanggal Film', 'Mulai', 'Selesai', 'Studio'])
        table.add_rows(fetch)
        return table

    def get_schedules_today(self):
        dateNow = date.today().strftime("%Y/%m/%d")
        sendDate = (dateNow,)

        read = 'SELECT schedules.id_schedule, movies.title, schedules.date_schedule, schedules.start, schedules.end, studios.studio_name FROM schedules INNER JOIN movies ON schedules.film_code = movies.code_film INNER JOIN studios ON schedules.id_studio = studios.id_studio WHERE schedules.date_schedule = %s'
        cursor.execute(read, sendDate)
        fetch = cursor.fetchall()
        for data in fetch:
            self.temporary_data.append(data)
        table = PrettyTable(['ID Jadwal', 'Nama Film', 'Tanggal Film', 'Mulai', 'Selesai', 'Studio'])
        table.add_rows(fetch)
        return table

    def get_chairs_free(self, thisStudio):
        thisStudios = thisStudio
        read = 'SELECT chairs.id_chair, chairs.chair_number, studios.studio_name FROM chairs INNER JOIN studios ON chairs.studio_id = studios.id_studio WHERE chairs.status = 0 AND studios.studio_name = %s'
        cursor.execute(read, (thisStudios, ))
        fetch = cursor.fetchall()
        for data in fetch:
            self.temporary_data.append(data)
        table = PrettyTable(['ID Kursi', 'Nomor Kursi', 'Nama Studio'])
        table.add_rows(fetch)
        return table