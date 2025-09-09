def srv(s1, s2):
    if len(s2) < len(s1):
        print(f'Сначала идет: {s1}')             ## сравнение длин строк в обратном порядке
        print(f'Потом идёт: {s2}')
        return
    elif len(s2) > len(s1):
        print(f'Сначала идет: {s2}')
        print(f'Потом идёт: {s1}')
        return
    for i in range(len(s1)):
        if s1[i] < s2[i]:
            print(f'Сначала идет: {s2}')
            print(f'Потом идёт: {s1}')            ## сравнение в обратном порядке
            return
        elif s1[i] > s2[i]:
            print(f'Сначала идет: {s1}')
            print(f'Потом идёт: {s2}')
            return
    print('Строки равны')      ## если до сюда дошло, значит строки одинаковые
    return

s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
srv(s1, s2)