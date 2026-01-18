from person import Owner
import random


class VetHospital:
    def __init__(self, doctors=[]):
        self.doctors = doctors

    def __str__(self):
        return f'{self.__class__.__name__}: {self.doctors}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.doctors})'

    def append_doctor(self, doctor):
        self.doctors.append(doctor)
        doctor.work_place = self

    def remote(self, doctor):
        try:
            self.doctors.remove(doctor)
        except ValueError:
            print('Данный врач не работал в ветеринарной клинике')

    def accept_pet(self, pet):
        if self.doctors:
            doctor_ind = random.randint(0, len(self.doctors) - 1)
            doctor = self.doctors[doctor_ind]
            doctor.conducting_reception(pet)
        else:
            print('Врачи отсутствуют')

    def give_pay(self, price, pet):
        if pet.owner.money < price:
            print('Недостаточно денежных средств')
        else:
            pet.owner.money -= price
            print(f'{pet.owner.first_name} оплатил лечение своему питомцу {pet.name} на сумму {price}')

class Vet(Owner):
    def __init__(self, first_name: str, last_name: str, pets: list, work_place: VetHospital):
        super().__init__(first_name, last_name, pets)
        self.work_place = work_place

    def conducting_reception(self, pet):
        price = random.randint(100, 10_000)
        print(f'Осмотр животного, {pet.name}, проводит ветеринар, {self.first_name} {self.last_name}')
        if not len(pet.pain):
            print(f'Животное {pet.name} здорово')
        else:
            pain = pet.pain.pop()
            if not len(pet.pain):
                print(f'У животного, {pet.name}, прошла боль в {pain}, теперь оно здорово')
            else:
                print(f'У животного, {pet.name}, прошла боль в {pain}')
        print(f'Итоговая стоимость лечения: {price}')
        self.work_place.give_pay(price, pet)



if __name__ == '__main__':
    doctor1 = Vet('Иван', 'Иванов', [], None)
    doctor2 = Vet('Михаил', 'Иванов', [], None)
    hospital = VetHospital()
    hospital.append_doctor(doctor1)
    hospital.append_doctor(doctor2)
    print(hospital)
    print(doctor1.work_place)