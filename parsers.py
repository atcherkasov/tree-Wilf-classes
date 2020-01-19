def parser(path='../equations.txt'):
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
    return groups
