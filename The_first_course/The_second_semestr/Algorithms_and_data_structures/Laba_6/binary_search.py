def cicle_version(mas, x):
    left,right = 0, len(mas)
    if (len(mas) and mas[0] == x):
         return 0
    while right - left > 1:
        mid = (left + right) // 2
        if mas[mid] < x:
            left = mid
        elif mas[mid] > x:
            right = mid
        else:
            return mid
    return -1

def recursion_version(mas, x, left, right):
    if len(mas) and mas[0] == x: return 0
    if not len(mas) or right - left <= 1: return -1
    mid = (left + right) // 2
    if mas[mid] == x:
        return mid
    elif mas[mid] < x:
        return recursion_version(mas, x, mid, right)
    else:
        return recursion_version(mas, x, left, mid)
    
    
def test_circle_version():
    mas = [1, 2, 4, 5, 6, 7, 8]
    tests = [1, 3, 4, 7]
    results = [0, -1, 2, 5]
    for ind in range(len(tests)):
        test, result = tests[ind], results[ind]
        circle_input = cicle_version(mas, test)
        recursion_input = recursion_version(mas, test, 0, len(mas))
        if circle_input != result or recursion_input != result:
            raise Exception(f"Провал теста: \nОжидал {result} \
                            \nПолучил: {circle_input} {recursion_input}")
        print(f"Входные данные: {test} -> {result}")

test_circle_version()