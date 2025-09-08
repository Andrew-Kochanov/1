n = int(input('До какого числа "рисовать" решето Эратосфена: ')) ##определяем промежуток от 2 до n
numbers = [i for i in range(2, n + 1)]     ##создание списка от 2 до n
temporary = numbers[0]   ## запоминаем текущее число
while temporary != numbers[-1]:
    numbers_fals = list()      ##создаем список чисел кратных текущему
    for i in range(numbers.index(temporary) + 1, len(numbers)):
        if numbers[i] % temporary == 0:        ##добавляем их туда
            numbers_fals.append(numbers[i])
    for k in range(len(numbers_fals)):
        numbers.remove(numbers_fals[k])    ##удаляем из общего списка
    temporary = numbers[numbers.index(temporary) + 1]   ## берем следующее число
print(f'Простые числа от 2 до {n}:', *numbers)