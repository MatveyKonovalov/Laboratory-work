import random
from help_funcs import get_statistics
from bst import BinarySearchTree
from avl import AVLTree
import matplotlib.pyplot as plt
import sys
import math

sys.setrecursionlimit(9_999_999)
def create_analitics(n: int, p: float):

    # Создаём отсортированный массив
    arr = list(range(n))

    # Перемешиваем часть элементов
    for i in range(n):
        if random.random() > p:  # c вероятностью (1-p) меняем местами
            j = random.randint(0, n-1)
            arr[i], arr[j] = arr[j], arr[i]
    return arr


def create_data():
    data_set = [None] * 100

    N = 10_000
    for p in range(0, 100):
        data_set[p] = create_analitics(n = N, p = p / 100)

    return data_set


def analitics():
    avl_res = []
    bst_res = []
    data_set = create_data()

    for data in data_set:
        avl = AVLTree()
        bst = BinarySearchTree()

        avl_res.append(get_statistics(data, avl))
        bst_res.append(get_statistics(data, bst))
    
    return (avl_res, bst_res)

def return_mases(mas):
    average = []
    times = []
    max_depth = []

    for i in mas:
        average.append(i[0])
        times.append(i[2])
        max_depth.append(i[1])
    return (average, max_depth, times)


def make_graph():
    avl, bst = analitics()

    average_avl, max_depth_avl, times_avl = return_mases(avl)
    average_bst, max_depth_bst, times_bst = return_mases(bst)

    x = list(map(lambda x: x / 100, range(100)))
    
    fig, axes = plt.subplots(2, 3, figsize=(20, 16))
    
    fig.suptitle("Сравнение BST и AVL (использовались массивы по 10_000 элементов)")
    axes[0, 0].plot(x, average_avl, "b", label="AVL")
    axes[0, 0].plot(x, average_bst, "r", label="BST")
    axes[0, 0].legend()
    axes[0, 0].set_title("Зависимость средней глубины\n от сортированности дерева")
    axes[0, 0].set_xlabel("Процент сортированности")
    axes[0, 0].set_ylabel("Количество вершин")

    axes[1, 0].plot(x, list(map(lambda x, y: y / x, average_avl, average_bst)), "b", label="Отношение")
    axes[1, 0].legend()
    #axes[1, 0].set_title("Отношение среднего количества вершин у AVL и BST")
    axes[1, 0].set_xlabel("Процент сортированности")
    axes[1, 0].set_ylabel("Соотношение: BST / AVL")

    axes[0, 1].plot(x, max_depth_avl, "b", label="AVL")
    axes[0, 1].plot(x, max_depth_bst, "r", label="BST")
    axes[0, 1].legend()
    axes[0, 1].set_title("Зависимость максимальной глубины\n от сортированности дерева")
    axes[0, 1].set_xlabel("Процент сортированности")
    axes[0, 1].set_ylabel("Количество вершин")

    axes[1, 1].plot(x, list(map(lambda x, y: y / x, max_depth_avl, max_depth_bst)), "b", label="Отношение")
    axes[1, 1].legend()
    #axes[1, 1].set_title("Отношение среднего количества вершин у AVL и BST")
    axes[1, 1].set_xlabel("Процент сортированности")
    axes[1, 1].set_ylabel("Соотношение: BST / AVL")
    

    axes[0, 2].plot(x, times_avl, "b", label="AVL")
    axes[0, 2].plot(x, times_bst, "r", label="BST")
    axes[0, 2].legend()
    axes[0, 2].set_title("Зависимость времени\n от сортированности дерева")
    axes[0, 2].set_xlabel("Процент сортированности")
    axes[0, 2].set_ylabel("Время (с)")

    axes[1, 2].plot(x, list(map(lambda x, y: x / y, times_avl, times_bst)), "b", label="Отношение")
    axes[1, 2].plot(x, [1] * 100, "g--", label="Ось равенства")
    axes[1, 2].legend()
    #axes[1, 2].set_title("Отношение среднего количества вершин у AVL и BST")
    axes[1, 2].set_xlabel("Процент сортированности")
    axes[1, 2].set_ylabel("Соотношение: AVL / BST")

    plt.show()

if __name__ == "__main__":
    make_graph()
# python create_data.py