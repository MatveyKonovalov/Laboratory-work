def main():
    eng = 'qwertyuiop[]asdfghjkl;\'zxcvbnm,./ ' 
    rus = 'йцукенгшщзхъфывапролджэячсмитьбю. '

    input_u = input("Введите строку: ")
    res = []
    for i in input_u:
        ind_eng = eng.find(i.lower())
        if ind_eng != -1:
            res.append(rus[ind_eng])

    print("".join(res))

if __name__ == "__main__":
    main()