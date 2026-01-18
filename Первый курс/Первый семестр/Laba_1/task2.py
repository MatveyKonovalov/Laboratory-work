import random

# n = random.randint(1, 10)
# test = [random.randint(-1000, 1000) for _ in range(n)]
test = [100,100, 90, 80, 70]
n = len(test)
test.sort(reverse=True)
print(f'test: {test}')
num = int(input("Введите число: "))

begin, end = 0, n

if num > test[0]:
    test = [num] + test
    print(test, 0)
elif num < test[-1]:
    test = test + [num]
    print(test, n)
else:
    while begin < end:
        mid = (begin + end) // 2
        # Можно сделать условие >= и убрать elif, но я решил сохранить структуру binary search
        if test[mid] == num:
            begin = mid + 1
        elif test[mid] > num:
            begin = mid + 1
        else:
            end = mid

    test.insert(begin, num)
    print(f'result: {test} {begin}')


