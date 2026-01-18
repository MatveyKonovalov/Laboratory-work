import random
n = random.randint(1, 10)
test = [random.randint(-100, 100) for _ in range(n)]
print(f'test: {test}')
del_num = None
fl_k = None
fl_no = True
i = 0
while i < len(test) - 1:
    if test[i] >= test[i+1]:
        # Если невыполнение условия возникало раньше, то завершаем цикл
        if not del_num is None:
            fl_no = False
            break
        begin_i = i
        # Если условие не выполняется в конце списка, а до этого ошибки не возникало, удаляем последний элемент
        if i + 1 == len(test) - 1:
            del_num = test[i+1]
            fl_k = True
            break
        if test[i] < test[i+2]:
            del_num = test[i+1]
            i += 2
        elif i > 0 and test[i+1] > test[i-1]:
            del_num = test[i]
            i += 1
        elif i == 0:
            del_num = test[i]
            i += 1
        if begin_i == i:
            fl_no = False
            break
    else:
        i += 1
if fl_k or fl_no:
    # Если список и так отсортирован, удаляем последний
    if del_num is None and len(test) > 1:
        del_num = test[-1]
    print(f'true ({del_num})')
else:
    print('false')