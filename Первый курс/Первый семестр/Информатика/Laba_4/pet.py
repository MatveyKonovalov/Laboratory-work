class PetFood:
    def __init__(self, name, not_hungry):
        self.name = name
        self.not_hungry = not_hungry

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, {self.not_hungry}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.not_hungry})'


class Pet:
    def __init__(self, name: str, breed: str, pain: list, owner):
        self.name = name
        self.breed = breed
        self.pain = pain
        self.owner = owner
        self.steps = 0
        self.happiness = 0
        self.hungry = 0

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, {self.breed}, {self.pain}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.breed}, {self.pain})'

    def up_hungry(self, cnt: int):
        self.hungry += cnt

    def get_happy(self, cnt: int):
        self.happiness += cnt

    def eat(self, food_product):
        self.get_happy(50)
        self.hungry += food_product.not_hungry


if __name__ == '__main__':
    dog = Pet('Bobik', 'Laborador', [], None)
    print(dog)
    milk = PetFood('milk', 15)
    print(milk)
    print([milk])
