n = int(input('До какого числа "рисовать" решето Эратосфена: ')) ##определяем промежуток от 1 до n
cqrt = int(n**0.5) ##целочислнный корень от n(нужен для "красивого вывода")
numbers = [i for i in range(1, n + 1)]##список чисел от 1 до n
count = 1  ##количество пройденных в цикле чисел
numbers[0] = 0     ## сразу меняем 1 на 0
while count < n:
    temporary = numbers[count]   ##запоминаем текущее число
    for i in range(count + 1, len(numbers)):
        if temporary != 0:   ##проверяем какие числа ему кратны и меняем на 0
            if numbers[i] % temporary == 0:
                numbers[i] = 0
        else:
            continue   ##чтоб не приходилось проверять деление на 0, скипаем 0
    count += 1

for i in range(cqrt):
    for j in range(cqrt):
        print(f'%{len(str(n)) + 1}d' % numbers[i * cqrt + j], end = ' ')   ##красивый вывод
    print()

