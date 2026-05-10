import random
import time
from typing import List, Tuple


class NaturalMergeSort:
    """Естественная сортировка слиянием с подсчётом сравнений"""
    
    def __init__(self):
        self.comparisons = 0
    
    def reset_comparisons(self):
        self.comparisons = 0
    
    def find_runs(self, arr: List) -> List[Tuple[int, int]]:
      
        n = len(arr)
        if n == 0:
            return []
        
        runs = []
        start = 0
        
        for i in range(1, n):
            self.comparisons += 1
            if arr[i] < arr[i - 1]:  
                runs.append((start, i))
                start = i
        
        runs.append((start, n))  
        return runs
    
    def merge(self, arr: List, left1: int, right1: int, left2: int, right2: int, temp: List):

        i, j, k = left1, left2, left1
        
        while i < right1 and j < right2:
            self.comparisons += 1
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        
    
        while i < right1:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j < right2:
            temp[k] = arr[j]
            j += 1
            k += 1
        
    
        for k in range(left1, right2):
            arr[k] = temp[k]
    
    def natural_merge_sort(self, arr: List) -> List:

        self.reset_comparisons()
        n = len(arr)
        
        if n <= 1:
            return arr
        
        temp = [0] * n
        
        while True:
            runs = self.find_runs(arr)
            
            if len(runs) == 1:
                break
            
            new_runs = []
            i = 0
            while i < len(runs):
                if i + 1 < len(runs):
                    start1, end1 = runs[i]
                    start2, end2 = runs[i + 1]
                    self.merge(arr, start1, end1, start2, end2, temp)
                    new_runs.append((start1, end2))
                    i += 2
                else:
                    new_runs.append(runs[i])
                    i += 1
            
            runs = new_runs
        
        return arr
    
    def classic_merge_sort(self, arr: List, left: int = 0, right: int = None, temp: List = None) -> List:
        if right is None:
            right = len(arr)
            temp = [0] * len(arr)
        
        if right - left <= 1:
            return arr
        
        mid = (left + right) // 2
        
        self.classic_merge_sort(arr, left, mid, temp)
        self.classic_merge_sort(arr, mid, right, temp)
        
        # Слияние
        i, j, k = left, mid, left
        while i < mid and j < right:
            self.comparisons += 1
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        
        while i < mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        
        while j < right:
            temp[k] = arr[j]
            j += 1
            k += 1
        
        for k in range(left, right):
            arr[k] = temp[k]
        
        return arr


class QuickSortWithComparisons:
    
    def __init__(self):
        self.comparisons = 0
    
    def reset_comparisons(self):
        self.comparisons = 0
    
    def quick_sort(self, arr: List, left: int = 0, right: int = None) -> List:
        if right is None:
            right = len(arr) - 1
        
        if left >= right:
            return arr
        
        mid = (left + right) // 2
        if arr[left] > arr[mid]:
            arr[left], arr[mid] = arr[mid], arr[left]
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[mid] > arr[right]:
            arr[mid], arr[right] = arr[right], arr[mid]
        
        pivot = arr[mid]
        arr[mid], arr[right - 1] = arr[right - 1], arr[mid]
        

        i = left
        for j in range(left, right):
            self.comparisons += 1
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        
        arr[i], arr[right] = arr[right], arr[i]
        
        self.quick_sort(arr, left, i - 1)
        self.quick_sort(arr, i + 1, right)
        
        return arr


def generate_arrays(size: int):
    """Генерирует тестовые массивы"""
    random_arr = [random.randint(0, 1000000) for _ in range(size)]
    sorted_arr = list(range(size))
    reversed_arr = list(range(size, 0, -1))
    
    return {
        "Случайный": random_arr,
        "Упорядоченный": sorted_arr,
        "Обратно упорядоченный": reversed_arr
    }


def run_benchmark(sizes: List[int]):
    """Запуск сравнения алгоритмов"""
    
    print("=" * 100)
    print(f"{'Размер'} | {'Тип массива'} | {'Natural Merge'} | {'Classic Merge'} | {'Quick Sort'}")
    print("=" * 100)
    
    natural_sorter = NaturalMergeSort()
    classic_sorter = NaturalMergeSort()
    quick_sorter = QuickSortWithComparisons()
    
    for size in sizes:
        arrays = generate_arrays(size)
        
        for arr_type, original_arr in arrays.items():
            # Natural Merge Sort
            arr1 = original_arr.copy()
            natural_sorter.reset_comparisons()
            natural_sorter.natural_merge_sort(arr1)
            natural_comps = natural_sorter.comparisons
            
            # Classic Merge Sort
            arr2 = original_arr.copy()
            classic_sorter.reset_comparisons()
            classic_sorter.classic_merge_sort(arr2)
            classic_comps = classic_sorter.comparisons
            
            # Quick Sort
            arr3 = original_arr.copy()
            quick_sorter.reset_comparisons()
            quick_sorter.quick_sort(arr3)
            quick_comps = quick_sorter.comparisons
            
            print(f"{size} | {arr_type} | {natural_comps} | {classic_comps} | {quick_comps}")
        
        print("-" * 100)


def verify_correctness():
    """Проверка корректности сортировки"""
    test_sizes = [0, 1, 10, 100]
    
    for size in test_sizes:
        for arr_type in ["Случайный", "Упорядоченный", "Обратно упорядоченный"]:
            arr = generate_arrays(size)[arr_type]
            original = arr.copy()
            
            sorter = NaturalMergeSort()
            sorted_arr = sorter.natural_merge_sort(arr.copy())
            
            expected = sorted(original)
            
            if sorted_arr == expected:
                print(f"{arr_type} массив размером {size}: OK")
            else:
                print(f"{arr_type} массив размером {size}: FAILED")
                print(f"  Было: {original}")
                print(f"  Стало: {sorted_arr}")
                print(f"  Ожидалось: {expected}")


if __name__ == "__main__":
    print("Проверка корректности:")
    print("-" * 50)
    verify_correctness()
    print()
    
    sizes = [10, 100, 1000, 10000]
    run_benchmark(sizes)