# Функции для сравнения в сортировках
def equal_func_sort(student1, student2):
    '''Функция для сравнения по нескольким параметрам'''
    if (student1[1] == student2[1]): # если предметы одинаковы
        if (student1[2] == student2[2]): # если баллы одинаковы
            return student1[0] < student2[0] 
        return student1[2] > student2[2]
    return student1[1] < student2[1]

def equal_func_find(student1, student2):
    '''Подходит ли студент по предмету и оценке'''
    if (student1[1] != student2[1]): # если предметы одинаковы
        return student1[1] < student2[1] 
    return student1[2] > student2[2]

# Бин поиск
def binary_search(mas, x, right, sort_func = equal_func_sort):
    '''Бинарный поиск для работы сортировки'''
    left = 0
    while left < right:
        mid = (left + right) // 2
        if sort_func(mas[mid], x):
            left = mid + 1
        else:
            right = mid
    return left # Если не было найдено возвращает right

def insert_sort(mas, sort_func = equal_func_sort):
    '''Функция сортировки'''
    for i in range(1, len(mas)):
        x = mas[i]
        insert_pos = binary_search(mas, x, i, sort_func=sort_func)
        
        for j in range(i, insert_pos, -1):
            mas[j] = mas[j - 1]
        
        mas[insert_pos] = x

def search_in_sorted_mas(mas, subject, grade):
    start_index = binary_search(mas, (None, subject, grade), right=len(mas), sort_func=equal_func_find)
    result = []
    while mas[start_index][1] == subject and mas[start_index][2] == grade:
        result.append(mas[start_index])
        start_index += 1
    return result

def average_grade(mas):
    hashtable = {} # subject: [cnt, len]
    for student in mas:
        if student[1] in hashtable:
            hashtable[student[1]] = [hashtable[student[1]][0] + student[2], hashtable[student[1]][1] + 1]
        else:
            hashtable[student[1]] = [student[2], 1]
            
    keys = list(hashtable.keys())
    insert_sort(keys, lambda x, y: x < y)

    for i, subject in enumerate(keys):
        data = hashtable[subject]
        print(f"{i+1}: {subject} {data[0] / data[1]:.2f}")


def get_top_student(mas):
    # student: [sum_grade, cnt_subject]
    student_average = {}
    for name, subject, grade in mas:
        if name in student_average:
            value = student_average[name]
            student_average[name] = [value[0] + grade, value[1] + 1]
        else:
            student_average[name] = [grade, 1]


    # [name, average_grade]
    first = [None, -1]
    second = [None, -1]
    third = [None, -1]

    for student in student_average.keys():
        val = student_average[student]
        grade = val[0] / val[1]
        if grade >= first[1]:
            third = [second[0], second[1]]
            second = [first[0], first[1]]
            first = [student, grade]
        elif grade >= second[1]:
            third = [second[0], second[1]]
            second = [student, grade]
        elif grade >= third[1]:
            third = [student, grade]
    for i, mas in enumerate([first, second, third]):
        if not mas[0]:
            break
        print(f"{i}. {mas[0]}: {mas[1]:.2f}")

    
    
    
        

def main():
    mas = [
        ("Иванов", "Математика", 85),
        ("Петров", "Физика", 92),
        ("Сидоров", "Математика", 78),
        ("Иванов", "Физика", 90),
        ("Петров", "Математика", 88),
        ("Сидоров", "Информатика", 95),
        ("Иванов", "Информатика", 82),
        ("Петров", "Информатика", 97),
        ("Сидоров", "Физика", 85),
        ("MyTest", "Математика", 85)
    ]
    insert_sort(mas)
    print(*mas, sep='\n')
    print()

    print(search_in_sorted_mas(mas, "Математика", 85))
    print()

    average_grade(mas)
    print()

    get_top_student(mas)
    print()

main()