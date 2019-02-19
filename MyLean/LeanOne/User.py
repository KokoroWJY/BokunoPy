class User():

    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def describe_user(self):
        print(str(self.first_name).title() + " " + str(self.last_name.title()))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def printOne(self):
        print(self.login_attempts)


Virus = User("w", "jy", 20)
Virus.describe_user()

VirusT = User("w", "jy", 20)
VirusT.increment_login_attempts()
VirusT.increment_login_attempts()
VirusT.increment_login_attempts()
VirusT.increment_login_attempts()
VirusT.printOne()
VirusT.reset_login_attempts()
VirusT.printOne()


class Privileges():

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add pist", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("管理员的全县有: ")
        for i in range(3):
            print(self.privileges[i])


class Admin(User):

    def __init__(self, first_name, last_name, login_attempts):
        super(Admin, self).__init__(first_name, last_name, login_attempts)
        self.privilegesOther = Privileges()


AdminOne = Admin('W', 'J', 20)
AdminOne.privilegesOther.show_privileges()
