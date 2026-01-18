import random

class Owner:
    def __init__(self, first_name: str, last_name: str, pets: list):
        self.first_name = first_name
        self.last_name = last_name
        self.pets = pets

        self.money = 0
        self.steps = 0

    def __str__(self):
        return f'{self.__class__.__name__}: {self.first_name}, {self.last_name}, {len(self.pets)}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.first_name}, {self.last_name}, {len(self.pets)})'

    def __chek_pet_in_pets(self, pet):
        if pet not in self.pets:
            print('Данный питомец отсутствует')
            return 0
        return 1

    def walk(self, pet):
        a, b = 1, 1000
        cnt_step = random.randint(a, b)
        self.steps += cnt_step
        pet.steps += cnt_step * 4
        pet.get_happy(10)
        print(f'{self.first_name} {self.last_name} выгуливает {pet.name} ({pet.breed})')

    def eat(self, pet, food_product):
        pet.eat(food_product)
        print(f'{self.first_name} {self.last_name} кормит {pet.name} ({pet.breed})')

    def stroke(self, pet):
        if self.__chek_pet_in_pets(pet):
            pet.get_happy(5)

    # Приём у ветеринара
    def go_vet(self, pet, hospital):
        if self.__chek_pet_in_pets(pet):
            pet.get_happy(-40)
            print(f'{self.first_name} {self.last_name} ведёт питомца {pet.name} к ветеринару')
            hospital.accept_pet(pet)
