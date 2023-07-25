current = int(input('Введите номер вагона по порядку следования: '))
vagon = int (input('Витя сел в вагон номер: '))
if current == vagon:
    print ('Не хватает информации')
else:
    print(f'Количество вагонов = {current + vagon}')