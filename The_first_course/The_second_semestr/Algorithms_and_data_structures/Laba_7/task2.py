import random
import time

# Быстрая сортировка
def quick_sort(mas): # Не оптимизированная
    if not mas:
        return []
    element = mas[0]
    bigger = []
    lower = []
    for el in mas[1:]:
        if element > el:
            lower.append(el)
        else:
            bigger.append(el)
    return quick_sort(lower) + [element] + quick_sort(bigger)

def quick_sort_optim(mas, left=0, right=None):
    if right is None: right = len(mas) - 1

    if left >= right:
        return 
    
    try:
        pivot = random.randint(left, right)
    except:
        return
    
    mas[left], mas[pivot] = mas[pivot], mas[left]

    head = left + 1
    end = right

    while head <= end:
        if mas[head] > mas[left]:
            mas[head], mas[end] = mas[end], mas[head]
            end -= 1
        else:
            head += 1
    mas[left], mas[end] = mas[end], mas[left]

    quick_sort_optim(mas, left, end - 1)
    quick_sort_optim(mas, end + 1, right)

# Сортировка слиянием
def merge_two_list(list1, list2): # Объединение двух осортированных массивов
    res = []

    ind1, ind2 = 0, 0
    while ind1 < len(list1) or ind2 < len(list2):
        if ind1 >= len(list1):
            res.extend(list2[ind2:])
            break
        elif ind2 >= len(list2):
            res.extend(list1[ind1:])
            break
        else:
            if list1[ind1] < list2[ind2]:
                res.append(list1[ind1])
                ind1 += 1
            else:
                res.append(list2[ind2])
                ind2 += 1
    return res

def merge_sort(mas): # Не оптимизированная
    if len(mas) == 1:
        return mas
    
    len_one_part = len(mas) // 2
    return merge_two_list(merge_sort(mas[:len_one_part]), merge_sort(mas[len_one_part:]))

### Оптимизированная merge sort
def merge_two_list_optim(arr, left, mid, right, temp):
    """
    Слияние двух отсортированных частей в temp с копированием обратно.
    Индексы: [left, mid) и [mid, right)
    """
    i, j, k = left, mid, left
    
    # Слияние
    while i < mid and j < right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    
    # Копирование остатков (быстро, без циклов)
    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    
    while j < right:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    # Копирование обратно в исходный массив
    for k in range(left, right):
        arr[k] = temp[k]


def merge_sort_optim(arr, left=0, right=None, temp=None):
    """
    In-place сортировка слиянием с одним временным массивом.
    Никаких копий и срезов!
    """
    if right is None:
        right = len(arr)
        temp = [0] * len(arr)
    
    if right - left <= 1:
        return
    
    mid = (left + right) // 2
    
    merge_sort_optim(arr, left, mid, temp)
    merge_sort_optim(arr, mid, right, temp)
    merge_two_list_optim(arr, left, mid, right, temp)
    
    return arr

def python_sort(mas):
    return sorted(mas)

# Подготовка к созданию тестов
def create_test_mas(k):
    test = [None] * k
    for num in range(k):
        test[num] = random.randint(-1000, 1000)
    return test

def get_time_work(mas, func):
    start = time.time()
    res = func(mas)

    return (res, (time.time() - start) * 1000)




def first_analitics():
    print("Анализ с неоптимизированными версиями")
    print()

    output_format = "Размер массива: {}\n" \
    "Метод\t\t\t|Время (мс)\nСортировка слиянием\t|{:.2f}\n" \
    "Быстрая сортировка\t|{:.2f}\nPython sorted()\t\t|{:.2f}"

    for cnt_el in 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6:
        testi = create_test_mas(cnt_el)
        quick = get_time_work(testi, quick_sort)
        merge = get_time_work(testi, merge_sort)
        python = get_time_work(testi, python_sort)
        if quick[0] == merge[0] and merge[0] == python[0]:
            print(output_format.format(cnt_el, quick[1], merge[1], python[1]))
            print()
        else:
            raise Exception("Сортированные списки не сошлись")
        
    print('=' * 20)

def second_analitics():
    print("\nАнализ с оптимизированными версиями\n")

    output_format = "Размер массива: {}\n" \
    "Метод\t\t\t|Время (мс)\nСортировка слиянием\t|{:.2f}\n" \
    "Быстрая сортировка\t|{:.2f}\nPython sorted()\t\t|{:.2f}"

    for cnt_el in 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6:
        testi = create_test_mas(cnt_el)
        quick = get_time_work(testi, quick_sort_optim)
        merge = get_time_work(testi, merge_sort_optim)
        python = get_time_work(testi, python_sort)
        print(output_format.format(cnt_el, quick[1], merge[1], python[1]))
        print()
        
    print('=' * 20)
if __name__ == "__main__":
    first_analitics()
    second_analitics()
