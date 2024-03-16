import csv

# словарь для перевода названия месяца
sl = {'01': 'Январь', '02': 'Февраль', '03': 'Март', '04': 'Апрель', '05': 'Май', '06': 'Июнь', '07': 'Июль',
      '08': 'Август', '09': 'Сентябрь', '10': 'Октябрь', '11': 'Ноябрь', '12': 'Декабрь'}
# словарь с счётчиком кол-во препаратов по месяцам
answer = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0}

# чтение и запись файла
with open('scientist.csv', encoding='utf-8') as file:
    with open('scientist_new.csv', newline='', encoding='utf-8', mode='w+') as output:
        reader = list(csv.reader(file, delimiter=','))
        for i, row in enumerate(reader):
            if i == 0:
                continue
            # увеличение кол-во рецептов, сделанных в опр. месяц
            answer[row[2].split('-')[1]] += 1
        writer = csv.writer(output, delimiter=',')
        writer.writerow(['month', 'count'])
        most_pop = [0, '']
        for i in answer:
            if answer[i] > most_pop[0]:
                # в переменной most_pop содержиться данные о месяце с максимальным кол-вом препаратов
                most_pop = [answer[i], sl[i]]
            writer.writerow([sl[i], answer[i]])
        file.close()
        output.close()

print(f'{most_pop[1]} наииболее благоприятен для ученых. В этом месяце было создано - {most_pop[0]} препарат(-а)')
