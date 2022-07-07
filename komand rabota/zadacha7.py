numbers = [2, 4, 7, 1, 8.4, -3.3, 7.1, -2, 4, -1, 7, -43, 8, -3, 6, 9]
a = []
b = []
for i in numbers:
    if i % 2 == 0:
        a.append(i)

        print('Четных чисел: ', len(a))
    else:
        b.append(i)
        print('Нечетных чисел: ', len(b))
