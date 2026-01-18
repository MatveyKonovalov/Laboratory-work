import random

n = random.randint(0, 10)
mas = [random.randint(0, 100) for _ in range(n)]

res = []
result = 'start {}\nresult: {}'

if not len(mas) or len(mas) == 1:
    print(result.format(mas, mas))
else:
    # for first
    if mas[0] > mas[-1] and mas[0] > mas[1]:
        res.append(mas[0])

    # 1 -> len(mas) - 1
    for i in range(1, len(mas) - 1):
        if mas[i] > mas[i - 1] and mas[i] > mas[i + 1]:
            res.append(mas[i])

    # for the last
    if mas[-1] > mas[-2] and mas[-1] > mas[0]:
        res.append(mas[-1])

    print(result.format(mas, res))
