user = int(input('Введите число'))+1
type_of_num = int(input('2 четное 1 нечетное'))

if type_of_num == 2:
    for i in range(1, user):
        if i % 2 == 0:
            print(i, end=' ')


if type_of_num == 1:
    for i in range(1, user):
        if i % 2 != 0:
            print(i, end=' ')

