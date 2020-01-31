def parser(path='input_files/equations_7.txt'):
    leaf_number = (path.split('_')[-1]).split('.')[0]

    file = open(path, 'r')

    groups = []
    group = []
    # разбиваем файл по группам из систем уравнений и их графиками
    for line in file:
        if line == '\n':
            groups.append(group[::])
            group = []
        else:
            group.append(line)

    # теперь в каждой группе(по факту это система уранений) разбиваем строки на массив из
    # переменных
    for group in groups:
        for i in range(1, len(group)):
            group[i] = [int(el) for el in group[i].split()]
    file.close()
    return groups, leaf_number
