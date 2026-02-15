import json


class Data:
    def __init__(self, name_file: str):
        self.name_file = name_file

    def open(self):
        with open(self.name_file) as f:
            data = json.load(f)
        return data

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name_file}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name_file})'


class Pet:
    def __init__(self, name, breed, pain):
        self.name = name
        self.breed = breed
        self.pain = pain

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}, {self.breed}, {self.pain}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.breed}, {self.pain})'





class Owner:
    def __init__(self, first_name: str, last_name: str, pets: list):
        self.first_name = first_name
        self.last_name = last_name
        self.pets = pets

    def __str__(self):
        return  f'{self.__class__.__name__}: {self.first_name}, {self.last_name}, {len(self.pets)}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.first_name}, {self.last_name}, {len(self.pets)})'

    def walk_eat_pets(self, pet, action):
        if pet in self.pets:
            print(f'{self.first_name} {self.last_name} {action} {pet.name} ({pet.breed})')
        else:
            print('Данный питомец отсутствует')

    # Приём у ветеринара
    def go_vet(self, pet, vet):
        if pet in self.pets:
            print(f'{self.first_name} {self.last_name} ведёт питомца {pet.name} к ветеринару {vet.first_name} '
                  f'{vet.last_name}')
            vet.conducting_reception(pet)
        else:
            print('Данный питомец отсутствует')


class Vet(Owner):
    def conducting_reception(self, pet):
        print(f'Осмотр животного, {pet.name}, проводит ветеринар, {self.first_name} {self.last_name}')
        if not len(pet.pain):
            print(f'Животное {pet.name} здорово')
        else:
            pain = pet.pain.pop()
            if not len(pet.pain):
                print(f'У животного, {pet.name}, прошла боль в {pain}, теперь оно здорово')
            else:
                print(f'У животного, {pet.name}, прошла боль в {pain}')


def main():
    d = Data('people_pets_pain.json')
    data = d.open()['people']
    people = []
    # Заполняем список, состоящий из классов Owner
    for human in data:
        human0 = Owner(human['first_name'], human['last_name'], [])
        for pet in human['pets']:
            human0.pets.append(Pet(pet['name'], pet['breed'], pet['pain']))
        people.append(human0)
    print(people)
    ###Демонстрация####
    # Создаем ветеринара
    vet = Vet("Алексей", "Ветеринаров", [])

    # Демонстрация на втором хозяине и его питомцах
    owner = people[1]
    for pet in owner.pets:
        print(f"\n1. Владелец: {owner}")
        print(f"2. Питомец: {pet.name} ({pet.breed})")
        print(f"3. Текущие боли: {pet.pain}")
        owner.walk_eat_pets(pet, "кормит")
        owner.walk_eat_pets(pet, "выгуливает")
        owner.go_vet(pet, vet)


main()
