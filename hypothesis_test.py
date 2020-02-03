def create_group(series):
    groups = []
    current_group = [series[0][1]]
    for i in range(len(series) - 1):
        if series[i][0] == series[i + 1][0]:
            current_group.append(series[i + 1][1])
        else:
            groups.append([series[i][0], current_group])
            current_group = [series[i + 1][1]]
    groups.append([series[len(series) - 1][0], current_group])
    groups = sorted(groups, key=lambda group: group[1][0])
    return groups


def groups_info(groups, name):
    print('Количество различный функций от ' + str(name) + ':', len(groups))
    print('Количество функций в группах: ', end='')
    for i in range(len(groups)):
        print(len(groups[i][1]), end=' ')
    print()
    for i in range(len(groups)):
        print(groups[i][0], end='')
        print(*groups[i][1])


def hyp_test(series_file_path='output_files/series_9_73.txt'):
    file = open(series_file_path, 'r')

    G = []
    F = []
    Graphs = []
    tact = 0
    for line in file:
        # print(line, end='')
        if tact % 4 == 0:
            Graphs.append([line, tact // 4])
        if tact % 4 == 1:
            G.append([line, tact // 4])
        if tact % 4 == 2:
            F.append([line, tact // 4])
        tact += 1
    G.sort()
    F.sort()
    G_groups = create_group(G)
    F_groups = create_group(F)
    groups_info(G_groups, 'G')
    print()
    print()
    print()
    groups_info(F_groups, 'F')

    if len(G_groups) != len(F_groups):
        print('Hypothesis in FALSE for given input')
    else:
        for i in range(len(G_groups)):
            if G_groups[i][1] != F_groups[i][1]:
                print('Hypothesis in FALSE for given input')
                return
        print('Hypothesis in TRUE for given input')


if __name__ == '__main__':
    hyp_test()