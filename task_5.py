import csv


def create_hash_table():
    '''Функция создания hash-таблицы

    Возраащает:
    hash-таблицу
    '''
    hash_table = {}
    with open('scientist.csv', encoding='utf-8') as file:
        reader = list(csv.reader(file, delimiter=','))
        file.close()
        for i, row in enumerate(reader):
            if i == 0:
                continue
            hash_table[row[1] + row[2]] = [row[0], row[3]]
        return hash_table


def search(name):
    '''Функция поиска по hash-таблице

    Описание аргументов:
    name -- имя препарата в формате: <Название препарата + дата создания препарата(ГГГГ-ММ-ДД)>
    '''
    if name in hash_table:
        print(f'Препарат создал {hash_table[name][0]}. Для препарата необходимы следующие ингредиенты: {hash_table[name][1]}')
    else:
        print('Такого препарата нет в базе')


def add(author, name, date, recipe):
    '''Функция добавления элемента в hash-таблицу

    Описание аргументов:
    author -- ФИО создателя препарата
    name -- Название препарата
    date -- Дата создания препарата(ГГГГ-ММ-ДД)
    recipe -- Список химических элементов, необходимых для создания препарата'''
    hash_table[name + date] = [author, ' '.join(recipe)]
    print('Препарат успешно добавлен')



# Создание таблицы
hash_table = create_hash_table()
# Поиск по таблице
search('Бетаин1236-02-18')
# Добавление в таблицу
add('Лебедев Фёдор Михайлович', 'Ураниум', '2012-01-29', ['Chemical_35', 'Chemical_69', 'Chemical_76'])
# Проверка добавления элемента в таблицу
search(search('Ураниум2012-01-29'))
