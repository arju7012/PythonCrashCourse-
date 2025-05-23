class Users:

    """Describing and greeting the users"""
    def __init__(self, first_name, last_name, username, mob_num):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.mob_num = mob_num
        self.login_attempts = 0

    def describe_user(self):
        print(f"Dear {self.first_name} {self.last_name}, your user name is {self.username} and mobile number is {self.mob_num}. You have login our website {self.login_attempts} times.")

    def greet_user(self):
        print(f"Welcome {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = Users('Arjun', 'p', 'arju', 8767677)
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.describe_user()
user_1.reset_login_attempts()
user_1.describe_user()

"""user_2 = Users('Vishnu', 'Babi', 'bobobo', 378458734)
user_2.describe_user()
user_2.greet_user()"""