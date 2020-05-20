def parse_series_file(series_file_path = '', directory_path = ''):
    """
    функця которая парсит на выбор: 1. файл с рядами
                                    2. дирректорию с файлами с рядами
    , на массивы с которыми уже можно работать

    формат в котором записаны ряды: 1. строчная запись графа
                                    2. ряд G
                                    3. ряд F
                                    4. пустая строка
                            либо
                                    1. время выполнения вычислений для данного шаблона
                                    2. строчная запись графа
                                    3. ряд G
                                    4. ряд F
                                    5. пустая строка

    :param series_file_path: путь к файлу с рядами
    :param directory_path: путь к дирректории с рядами
    :return: 3 массива: 1. массив со строчной записью графа
                        2. массив с рядами G
                        3. массив с рядами F
                        4. массив со временем выполнения times
    """

    G = []
    F = []
    Graphs = []
    times = []
    if directory_path == '':
        file = open(series_file_path, 'r')
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
    else:
        import os
        all_files = os.listdir(directory_path)
        cnt = 0
        for file_name in all_files:
            file = open(directory_path + '/' + file_name, 'r')
            s = file.readlines()
            times.append([s[0], cnt])
            Graphs.append([s[1], cnt])
            G.append([s[2], cnt])
            F.append([s[3], cnt])
            file.close()
            cnt += 1
    return Graphs, G, F, times


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


def hyp_test(series_file_path='', directory_path='', meta_mode=True):
    """
    основна функция проверки гипотезы
    :param series_file_path: основна функция проверки гипотезы
    :param directory_path: путь к дирректории с рядами
    :param meta_mode: выводить ли всю информацию в консоль?
    :return:
    """
    Graphs, G, F, times = parse_series_file(series_file_path, directory_path)

    G.sort()
    F.sort()

    G_groups = create_group(G)
    F_groups = create_group(F)
    print(len(G_groups))
    print(len(F_groups))

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
    hyp_test('', '../output_files/En_11_201')

    # hyp_test('../output_files/series_short_8_151.txt')
