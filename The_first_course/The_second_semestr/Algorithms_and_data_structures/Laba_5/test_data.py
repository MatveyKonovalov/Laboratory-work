from hashTable import HashTable
import random
import time
import matplotlib.pyplot as plt
import functools

def return_current_time(arg1=None):
    """Декоратор для измерения времени выполнения функции"""
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            return elapsed  # Возвращаем затраченное время
        return wrapper
    
    # Поддержка вызова без аргументов
    if callable(arg1):
        return actual_decorator(arg1)
    return actual_decorator

def make_test_hash(n : int, hashTabSize: int) -> HashTable:
    hashTab = HashTable(hashTabSize)
    for i in range(n):
        key = random.randint(1, 1_000_000)
        value = "a" * (i % 50)
        hashTab.add(key, value)

    return hashTab

@return_current_time
def search(hashTab: HashTable):
    try:
        hashTab.get(random.randint(0, 1000))
    except KeyError:
        pass
@return_current_time
def add(hashTab: HashTable):
    hashTab.add(random.randint(0, 10000), "qqq")

@return_current_time
def delin(hashTable: HashTable):
    hashTable.del_pair(random.randint(0, 1000))


def make_analitics():

    data_set = []

    for size in range(10, 10_000):
        hashi = make_test_hash(10_000, size)

        t_add = add(hashi)
        t_search = search(hashi)
        t_del = delin(hashi)

        k = float(hashi.return_k())
 
        data_set.append((k, t_add + t_del + t_search))

    return data_set

def make_mas_by_k(data_set, top, flood):
    res = filter(lambda x: flood < x[0] <= top, data_set)
    times = []
    info_k = []

    for ki, timei in res:
        times.append(timei)
        info_k.append(ki)
    return (info_k, times)
    
def make_graph(data_set):
    plt.xlabel("Коэффициент заполняемости")
    plt.ylabel("Сумарное время, которое занимают опреации")
    plt.title("Анализ скорости работы HashTab")

    green_zone = make_mas_by_k(data_set, 0.6, -1)
    orange_zone = make_mas_by_k(data_set, 0.8, 0.6)
    red_zone = make_mas_by_k(data_set, 1, 0.8)

    plt.plot(green_zone[0], green_zone[1], 'o', linestyle='none', color='green')
    plt.plot(orange_zone[0], orange_zone[1], 'o', linestyle='none', color='orange')
    plt.plot(red_zone[0], red_zone[1], 'o', linestyle='none', color='red')
    plt.show()

def save_data(data_set):
    with open("my_data1.txt", 'w') as f:
        for ki, timei in data_set:
            f.write(f"{ki} {timei}\n")


def main():
    data = make_analitics()
    save_data(data)
    make_graph(data)

if __name__ == "__main__":
    main()

