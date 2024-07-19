n = int(input('Введите число с первой вставки (от 3 до 20) '))
if n < 3 or n>20:
    print('Вас настигли шипы, вы не умеете читать...')
else:
    lst = []
    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                continue
            else:
                sum_ = i + j
                if n % sum_ == 0 and i<j:
                    lst1 = f'{i}{j}'
                    lst.append(lst1)
                else:
                    continue
    print('Ваш пароль', ''.join(lst))


