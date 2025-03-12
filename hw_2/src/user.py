class User:
    count = 0

    def __init__(self, name, age):
        self.check_input_name(name)
        self.check_input_age(age)
        self.name = name
        self.age = age
        User.count += 1

    def check_input_name(self, name):
        if not isinstance(name, str):
            raise TypeError()

        if len(name) < 1:
            raise ValueError()

    def check_input_age(self, age):
        if not isinstance(age, int):
            raise TypeError()

        if age < 1 or age > 100:
            raise ValueError()

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def up_age(self):
        self.age += 1
        return self.age

