def binary_search(mas, x, right):
    left = 0
    while left < right:
        mid = (left + right) // 2
        if mas[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left

def insert_sort(mas):
    for i in range(1, len(mas)):
        x = mas[i]
        insert_pos = binary_search(mas, x, i)
        
        for j in range(i, insert_pos, -1):
            mas[j] = mas[j - 1]
        
        mas[insert_pos] = x

def test():
    mas = [1, 4, 3, 8]
    insert_sort(mas)
    print(mas)  
    
    test_cases = [
        [5, 2, 8, 1, 9],
        [3, 3, 3, 1, 2],
        [1],
        [],
        [10, 9, 8, 7, 6]
    ]
    
    for test_case in test_cases:
        insert_sort(test_case)
        print(test_case)

test()