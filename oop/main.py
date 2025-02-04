

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(self.first_name, self.last_name, self.age)


user = User("John", "Doe", 22)
user.describe_user()

string = "Name"


