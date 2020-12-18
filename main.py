import os
import time
import userClass


permisi = userClass.permission(0)
login_status = False

while True:
    print('=+='*20)
    print('\t\t\t-LOGIN-')
    username = input('\t\tusername : ')
    password = input('\t\tpassword : ')
    print('=+='*20)
    permisi.get_users_data()
    for i in range(len(permisi.temporary_data)):
        if username in permisi.temporary_data[i]:
            if password in permisi.temporary_data[i]:
                login_status = True
                get_role = permisi.temporary_data[i][7]
                break
    if login_status == True:
        print('berhasil login')
        break
    else:
        print('username / password salah')

permisi.set_role_id(get_role)
loginn = userClass.login(username, password, permisi.role_id)
time.sleep(1)
if loginn.get_role() == 1:
    sadmin = userClass.admin(username, password, loginn.get_role())
    print('\n\t\t  -LOGIN as ADMIN-')
elif loginn.get_role() == 2:
    print('yolooo')

