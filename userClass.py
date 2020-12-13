import permission

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
    def __init__(self, id_user, name, email, password, gender, contact):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.password = password
        self.gender = gender
        self.contact = contact
    
    def add_user(self):
        pass

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