class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Dog(name={self.name!r},age={self.age!r},breed={self.breed!r})"

    def bark(self):
        return f"{self.name} says woof"

    

class Vaccine:

    def __init__(self, name, date, expire):
        self.name = name
        self.date = date
        self.expire = expire

