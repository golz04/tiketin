import connection
import mysql.connector

class roles:
    def __init__(self, id_role, role_name):
        self.id_role = id_role
        self.role_name = role_name
    
    def add_role(self):
        pass

    def edit_role(self):
        pass

    def delete_role(self):
        pass


class admin(roles):
    cursor = connection.db.cursor()
    def __init__(self, id_user, password):
        self.id_user = id_user
        self.password = password
    
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
        print('''
        id\t nama role
        1\t admin
        2\t costumer
        ''')
        role_id = int(input('masukan role id : '))

        sql = 'INSERT INTO users (id_user, name, email, password, gender, contact, address, role_id) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)'
        val = (name, email, password, gender, contact, alamat, role_id)
        try:
            self.cursor.execute(sql, val)
            connection.db.commit()
            print('input sukses')
        except:
            print('error gan')

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


if __name__ == "__main__":
    #tes drive aja ntar diapus ya ;)
    sadmin = admin(1,1)
    sadmin.add_user()
