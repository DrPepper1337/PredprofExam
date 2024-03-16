import csv


def read_csv():
    with open('scientist.csv', encoding='utf-8') as file:
        '''Функция чтения csv файла'''
        reader = list(csv.reader(file, delimiter=','))
        file.close()
        return reader


reader = read_csv()
for i, row in enumerate(reader):
    if i == 0:
        continue
    # формирование идентификатора
    id = row[0][:3].capitalize() + row[1][:3].capitalize() + row[2].split('-')[0]
    # добавление идентификатора в список
    reader[i].append(id)

# Запись списка в файл
with open('preparationt_id.csv', newline='', encoding='utf-8', mode='w+') as output:
    writer = csv.writer(output, delimiter=',')
    for i, row in enumerate(reader):
        if i == 0:
            continue
        writer.writerow(reader[i])
    output.close()
