import csv


def read_csv():
    with open('scientist.csv', encoding='utf-8') as file:
        '''Функция чтения csv файла'''
        reader = list(csv.reader(file, delimiter=','))
        file.close()
        return reader


# Цикл работает бесконечно, пока не будет введено слово: 'эксперимент'
reader = read_csv()
while 1:
    s = input()
    if s == 'эксперимент':
        # Выходим из цикла если было введено слово: 'эксперимент'
        break
    flag = True
    # Алгоритм линейного поиска по данным
    for row in reader:
        if s == row[1]:
            name = row[0].split()
            date = '.'.join(row[2].split('-')[::-1])
            # flag ставим в полоение False, ибо был найден такой элемент в данных
            flag = False
            print(f'Ученый {name[0] + " " + name[1][0] + "." + name[2][0] + "."} создал препарат: {date}')
            break
    if flag:
        # Выводим, что препарат не создан, если флаг в положении False, тоесть не найден в данных
        print('Этот препарат еще не создан')
