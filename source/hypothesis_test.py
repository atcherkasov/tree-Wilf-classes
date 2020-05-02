def parse_series_file(series_file_path: str):
    """
    функця которая парсит файл с рядами на массивы с которыми уже можно работать
    формат в котором записаны ряды: 1. строчная запись графа
                                    2. ряд G
                                    3. ряд F
                                    4. пустая строка
    :param series_file_path: путь к файлу с рядами
    :return: 3 массива: 1. массив со строчной записью графа
                        2. массив с рядами G
                        3. массив с рядами F
    """
    file = open(series_file_path, 'r')
    G = []
    F = []
    Graphs = []
    tact = 0
    for line in file:
        if tact % 4 == 0:
            Graphs.append([line, tact // 4])
        if tact % 4 == 1:
            G.append([line, tact // 4])
        if tact % 4 == 2:
            F.append([line, tact // 4])
        tact += 1
    file.close()
    return Graphs, G, F


def create_group(series: list) -> list:
    """
    функция которая разбивает данные из дефолтного файла series_n_len.txt
    :param series: list из строк. Каждая строка это ряд
    :return: отсортированный list, состоящий из кортежей - <ряд (str),
                                                            порятковый номер графа (int)>
    """
    groups = []
    current_group = [series[0][1]]
    for i in range(len(series) - 1):
        if series[i][0] == series[i + 1][0]:
            current_group.append(series[i + 1][1])
        else:
            groups.append((series[i][0], current_group))
            current_group = [series[i + 1][1]]
    groups.append((series[len(series) - 1][0], current_group))
    groups = sorted(groups, key=lambda group: group[1][0])
    return groups


def groups_info(groups: list, name: str):
    """
    выводит информацию по группам
    :param groups: массив с группами
    :param name: название группы (F или G)
    :return:
    """
    print('Количество различный функций от ' + str(name) + ':', len(groups))
    print('Количество функций в группах: ', end='')
    for i in range(len(groups)):
        print(len(groups[i][1]), end=' ')
    print()
    for i in range(len(groups)):
        print(groups[i][0], end='')
        print(*groups[i][1])


def hyp_test(series_file_path='output_files/series_9_73.txt', meta_mode=True):
    """
    основна функция проверки гипотезы
    :param series_file_path: основна функция проверки гипотезы
    :param meta_mode: выводить ли всю информацию в консоль?
    :return:
    """
    Graphs, G, F = parse_series_file(series_file_path)

    G.sort()
    F.sort()

    G_groups = create_group(G)
    F_groups = create_group(F)

    if meta_mode:
        groups_info(G_groups, 'G')
        print("\n\n\n\n\n\n\n")
        groups_info(F_groups, 'F')

    # проверка правильности гипотезы
    if len(G_groups) != len(F_groups):
        print('Hypothesis in FALSE for given input')
        return False
    else:
        for i in range(len(G_groups)):
            if G_groups[i][1] != F_groups[i][1]:
                print('Hypothesis in FALSE for given input')
                return False
        print('Hypothesis in TRUE for given input')
        return True


if __name__ == '__main__':
    # hyp_test('output_files/nice_series_9_101.txt')
    hyp_test('rubbish_files/short_nice_series_10_13.txt')
