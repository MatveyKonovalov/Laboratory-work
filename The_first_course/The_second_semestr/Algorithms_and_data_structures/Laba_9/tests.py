from random import randint
from help_funcs import get_statistics

def generate_random(n: int) -> list[int]:
    mas = [None] * n
    for i in range(n):
        mas[i] = randint(0, 1_000_000)
    return mas

def generate_sort(n: int) -> list[int]:
    mas = [None] * n
    for i in range(n):
        mas[i] = i
    return mas

def sequence(n: int) -> list[int]:
    mas = [1]
    for i in range(2, n, 2):
        mas.append(i + 1)
        mas.append(i)
    return mas

