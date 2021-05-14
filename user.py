import hashlib


class User:
    def __init__(self,username,hashed_password,role,major,no_units=0):
        self.username = username
        self.hashed_password = hashed_password
        self.role = role
        self.major = major
        self.no_units = no_units

    def register(self, user_info):
        user_info.append([self.username,self.hashed_password,self.role,self.major,self.no_units])

    def log_in(self,locked_users):
        counter = 0
        while True:
            entered_password = input('please enter your password: ')
            if hashlib.sha256(entered_password.encode('utf8')).hexdigest() == self.hashed_password:
                print('-----------------welcome------------------')
                return True
            elif counter == 2:
                print('your account is locked!')
                locked_users.append(f'{self.username}\n')
                return False
            else:
                print('wrong password!')
                counter += 1


    @staticmethod
    def is_locked(locked_users, username):
        for line in locked_users:
            if username == line.strip():
                print('your account is locked! you can not enter the system!')
                return True








