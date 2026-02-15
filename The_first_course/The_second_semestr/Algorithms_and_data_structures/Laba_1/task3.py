def sievesOfEr(a: int, b: int) -> list:
    if b < 2:
        return []

    start = max(2, a)
    
    sieve = [True] * (b + 1)
    sieve[0] = False
    sieve[1] = False
    
    for i in range(2, int(b ** 0.5) + 1):
        if sieve[i]: # Если sieve[i] простое, помечаем все числа кратные i
            for j in range(i * i, b + 1, i):
                sieve[j] = False

    # Формируем вохвращаемый список
    result = [num for num in range(start, b + 1) if sieve[num]]
    return result


def isPrime(num):
    if num == 2: 
        return True
    if num % 2 == 0 or num <= 1:
        return False
    d = 3
    while d * d <= num:
        if num % d == 0:
            return False
        d += 2
    return True


def makeIsPrime(a, b):
    result = []
    for i in range(a, b+1):
        if isPrime(i):
            result.append(i)
    return result


def main():
    try:
        a = int(input("Введите число a: "))
        b = int(input("Введите число b: "))
        if b < a:
            print("Некорректный ввод: a должно быть не больше b")
            return
        # #Проверка на совпадение ответа
        # res = []
        # res1 = []
        # data = sievesOfEr(a, b)
        # for num in range(b - a + 1):
        #     if data[num]:
        #         res.append(num + a)
        # for num in range(a, b + 1):
        #     if isPrime(num):
        #         res1.append(num)
        # print(res == res1)

        res = [] # Ответ
        # Если слишком большой промежуток значений -> Аналог решета Эратосфена
        if b - a > 100_000:
            res = sievesOfEr(a, b)
        # Если промежуток значений маленький
        else:
            res = makeIsPrime(a, b)

        print(f"Простые числа в диапазоне [{a}, {b}]: {res}")
        print(f"Количество простых чисел: {len(res)}")
    except ValueError:
        print("Некорректный ввод: a, b - Числа")

if __name__ == "__main__":
    main()
