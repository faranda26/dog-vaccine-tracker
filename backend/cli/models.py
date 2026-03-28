class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r})"


class Dog:

    def __init__(self, id, name, age, breed, owner_id):
        self.id = id
        self.name = name
        self.age = age
        self.breed = breed
        self.owner_id = owner_id

    def __repr__(self):
        return f"Dog(name={self.name!r},age={self.age!r},breed={self.breed!r})"

    def bark(self):
        return f"{self.name} says woof"

    

class Vaccine:

    def __init__(self, name, date, expire):
        self.name = name
        self.date = date
        self.expire = expire

