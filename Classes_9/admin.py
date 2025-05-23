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

class Admin(Users):
    """Showing privilages of admin."""

    def __init__(self, first_name, last_name, username, mob_num):
        super().__init__(first_name, last_name, username, mob_num)
        self.privileges = []

    def show_privileges(self):
        print("The privileges of admin are showned below.")
        for privilege in self.privileges:
            print(f"- He can {privilege}")



admin1 = Admin("sagar", "jacky", "sagaraliasjacky", 2255545)
admin1.privileges = ["kill you", "set you free", "place in prison"]
admin1.describe_user()
admin1.show_privileges()