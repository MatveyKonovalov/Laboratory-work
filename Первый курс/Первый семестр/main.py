from person import Owner
from pet import Pet, PetFood
from wet import Vet, VetHospital
from work_to_json import Data


def main():
    # Читаем данные из файла
    data = Data('people_pets_pain.json')
    file = data.open()['people']

    # Сохраняем и структурируем данные из файла
    people = []
    for i in file:
        owner = Owner(i['first_name'], i['last_name'], [])
        for pet in i['pets']:
            pet0 = Pet(pet['name'], pet['breed'], pet['pain'], owner)
            owner.pets.append(pet0)
        people.append(owner)
    print(people)

    ### Тесты ###

    # Создаём и добавляем врачей
    doctors = [Vet('Иван', 'Иванов', [], None),
               Vet('Александр', 'Иванов', [], None)]
    hospital = VetHospital()
    for i in doctors:
        hospital.append_doctor(i)

    # Создаём продукт
    corm = PetFood('RoyalCanin', 40)

    # Возьмём 2-го человека из списка people
    owner = people[1]
    owner.money = 100_000
    print(owner, '\n')
    for pet in owner.pets:
        print(pet)
        owner.walk(pet)
        owner.eat(pet, corm)
        owner.stroke(pet)
        owner.go_vet(pet, hospital)
        print()


if __name__ == '__main__':
    main()
