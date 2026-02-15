import random

# n = random.randint(1, 10)
# test = [random.randint(1, 100) for _ in range(n)]
test = [6, 1, 23, 9, 1, 5]
alone = set() # alone = []
for i in range(len(test)):
    if test[i] in alone:
        num = test.pop(i) # Сохраняем и удаляем элемент
        print(f'result: {test} {num} {i}')
        break
    else:
        alone.add(test[i]) #alone.append(test[i])
