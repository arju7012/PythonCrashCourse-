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
        self.privileges = Privileges()

class Privileges:
    """class to store admin privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        
        else:
            print("This user has no privileges.")


admin2 = Admin("leo", "harvin" ,"leoleoleo", 4577)
admin2.describe_user()
admin2.greet_user()

#admin2.privileges.show_privileges()

admin2_privileges = ["reset password", "edit profile"]
admin2.privileges.privileges = admin2_privileges
admin2.privileges.show_privileges()