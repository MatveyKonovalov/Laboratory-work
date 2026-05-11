from bst import BinarySearchTree
from avl import AVLTree
from tests import *
import sys

sys.setrecursionlimit(9_999_999)
def compare():
    k = 1_000

    mas1 = generate_random(k) 
    mas2 = generate_sort(k)
    mas3 = sequence(k) 
    name = [f"random({k})", f"sort({k})", f"seq({k})"]

    avl_res = []
    for data in mas1, mas2, mas3:
        l = AVLTree()
        avl_res.append(get_statistics(data, l))


    bst_res = []
    for data in mas1, mas2, mas3:
        l = BinarySearchTree()
        bst_res.append(get_statistics(data, l))

    print("|" + "=" * 83 + "|")
    print(f"|{'Критерий':^20}|{'BST':^20}|{'AVL':^20}|{'Type':^20}|")
    print("|" + "=" * 83 + "|")
    for ind in range(3):
        print(f"|{'Время построения':20}|{str(bst_res[ind][-1])[:5]:^20}|{str(avl_res[ind][-1])[:5]:^20}|{name[ind]:^20}|")
        print(f"|{'Средняя глубина':20}|{str(bst_res[ind][0])[:5]:^20}|{str(avl_res[ind][0])[:5]:^20}|{name[ind]:^20}|")
        print(f"|{'Максимальная глубина':20}|{bst_res[ind][1]:^20}|{avl_res[ind][1]:^20}|{name[ind]:^20}|")
        print("|" + "=" * 83 + "|")

if __name__ == "__main__":
    compare()