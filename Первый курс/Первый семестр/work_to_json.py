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


def test():
    data_handler = Data('people_pets_pain.json')
    data = data_handler.open()  # Используем метод класса
    print(data)


if __name__ == '__main__':
    test()
