def findall(n, currentelement):
    n += 1
    for j in range(currentelement, 12):
        number[n - 1] = j
        if j < 11:
            findall(n, j + 1)
        else:
            weight = 0
            value = 0
            # print(n)
            for i in range(n):
                weight += stufflist[number[i]][0]
                value += stufflist[number[i]][1]
            if (weight <= maxweight) and (value >= 100):
                print(number[:n])
    n -= 1


def get_all_points_count(stufflist):
    sum = 0
    for item in stufflist:
        sum += item[1]
    return sum


def get_items(stufflist, A):
    n = len(stufflist)  # находим размеры таблицы
    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            # заполняем первую строку
            if i == 0 or a == 0:
                V[i][a] = 0
            # если площадь предмета меньше площади столбца,
            # максимизируем значение суммарной ценности
            elif stufflist[i - 1][0] <= a:
                V[i][a] = max(stufflist[i - 1][1] +
                              V[i - 1][a - stufflist[i - 1][0]], V[i - 1][a])
            # если площадь предмета больше площади столбца,
            # забираем значение ячейки из предыдущей строки
            else:
                V[i][a] = V[i - 1][a]

    n = len(stufflist)
    res = V[n][A]  # начинаем с последнего элемента таблицы
    a = A  # начальная площадь - максимальная
    items_list = []  # список номеров предметов

    for i in range(n, 0, -1):  # идём в обратном порядке
        if res <= 0:  # условие прерывания
            break
        if res == V[i - 1][a]:  # ничего не делаем, двигаемся дальше
            continue
        else:
            # "забираем" предмет
            items_list.append(i)
            res -= stufflist[i - 1][1]  # отнимаем значение ценности от общей
            a -= stufflist[i - 1][0]  # отнимаем площадь от общей

    return items_list


stufflist = ((3, 25, 'в'), (2, 15, 'п'), (2, 15, 'б'),
             (2, 20, 'а'), (1, 5, 'и'), (1, 15, 'н'),
             (3, 20, 'т'), (1, 25, 'о'), (1, 15, 'ф'),
             (1, 10, 'д'), (2, 20, 'к'), (2, 20, 'р'))

itemslist = get_items(stufflist, 9)
answer = [['', '', ''], ['', '', ''], ['', '', '']]
i = 0
j = 0
points_count = 0    # Сумма очков оптимального набора
for n in itemslist:
    points_count += stufflist[n - 1][1]
    for k in range(stufflist[n - 1][0]):
        answer[i][j] = stufflist[n - 1][2]
        if j < 2:
            j += 1
        else:
            j = 0
            i += 1
for i in answer:
    print(i)
print('Итоговые очки выживания:', 10 - get_all_points_count(stufflist) + 2 * points_count)

itemslist = get_items(stufflist, 7)
points_count = 0
for n in itemslist:
    points_count += stufflist[n - 1][1]
print('Итоговые очки выживания:', 10 - get_all_points_count(stufflist) + 2 * points_count)

allpoints = get_all_points_count(stufflist)
number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
maxweight = 9
n = 0
findall(0, 0)
