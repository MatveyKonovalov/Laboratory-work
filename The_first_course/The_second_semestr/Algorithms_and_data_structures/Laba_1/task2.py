def printData(data: dict):
    print("Анализ чисел:")
    print(f"Максимальное значение: {data['max']}")
    print(f"Минимальное значение: {data['min']}")
    print(f"Среднее арифметическое: {data['average']}")
    print(f"Количество чётных чисел: {data['cntEven']}")
    print(f"Количество нечётных чисел: {data['cntNotEven']}")


def analyze_numbers(numbers: list) -> dict:
    data = {
        "max": numbers[0],
        "min": numbers[0],
        "average": None,
        "cntEven": 0,
        "cntNotEven": 0
    }
    smNums = 0
    cnt = 0

    for num in numbers:
        smNums += num
        cnt += 1

        if num > data["max"]:
            data["max"] = num
        if num < data["min"]:
            data["min"] = num

        if num % 2 == 0:
            data["cntEven"] += 1
        else:
            data["cntNotEven"] += 1
    data["average"] = float(f"{smNums / cnt:.2f}")

    return data

def main():
    try:
        mas = list(map(int, input("Введите числа через пробел: ").split()))
        data = analyze_numbers(mas)
        printData(data)
    except IndexError:
        data = {
        "max": None,
        "min": None,
        "average": None,
        "cntEven": 0,
        "cntNotEven": 0
        }
        print("Пустой ввод !!!")
        printData(data)
    except ValueError:
        print("Некорректный ввод !!!\nВведите числа через пробел")

if __name__ == "__main__":
    main()