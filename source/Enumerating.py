from source.get_series import combo_equations_to_series, beautiful_time
from source.poly_func.my_poly_functions import show_global
from source.parsers import parser
from source import parallel_setup
import os
import time


if __name__ == '__main__':

    # чтение конфига
    dots = '../'

    fin = open(dots + 'configs/Enumerating.txt', 'r')
    all_strings = fin.readlines()
    leaf_number = int(all_strings[11].split()[0])
    x_len = int(all_strings[12].split()[0])
    start_fold = int(all_strings[13].split()[0])
    end_fold = int(all_strings[14].split()[0])
    handle = all_strings[15].split()[0]

    parallel_setup.init()

    start = time.time()
    groups, leaf_number = parser(dots + 'input_files/equations_short_' + str(leaf_number) + '.txt')

    if start_fold > end_fold:
        change = -1
        start_fold = min(start_fold, len(groups))
    else:
        change = 1
        end_fold = min(end_fold, len(groups))

    out_dir_path = dots + 'output_files/En_' + str(leaf_number) + '_' + str(x_len)
    try:
        os.mkdir(out_dir_path)
    except:
        pass

    log_dir_path = dots + 'loges/En_' + str(leaf_number) + '_' + str(x_len)
    try:
        os.mkdir(log_dir_path)
    except:
        pass

    loges_file = open(log_dir_path + '/' + handle + '_from_' + str(min(start_fold, end_fold)) + '_to_' + str(max(start_fold, end_fold)) + '.txt', 'w')

    part = 5.0
    part_time = part

    already_counted_folds = set([int(file_name[:file_name.find('_')]) for file_name in os.listdir(out_dir_path)])
    indexes = set(range(start_fold, end_fold, change)) - already_counted_folds
    indexes = sorted(list(indexes))
    local_ind = -1
    for i in indexes:
        local_ind += 1
        lit_start = time.time()
        x_series, xy_series = combo_equations_to_series(groups[i][1:], [(x_len + 1) // 2,])
        file = open(out_dir_path + '/' + str(i) + '_fold_' + handle + '.txt', 'w')
        print(time.time() - lit_start, file=file)
        print(groups[i][0][:-1], file=file)
        print(show_global(x_series), file=file)
        print(show_global(xy_series), file=file)

        percent = round(local_ind / float(len(indexes)) * 100, 1)
        if percent >= part_time:
            print('посчитанно', str(percent) + '%. За',
                  beautiful_time(time.time() - start), file=loges_file)
            print('посчитанно', str(percent) + '%. За',
                  beautiful_time(time.time() - start))

            part_time += part
        else:
            print(percent, '%')
        file.close()

    print(' ВЕСЬ ПРОЦЕСС ЗАНЯЛ: ' + beautiful_time(time.time() - start),
          file=loges_file)
    print('заняло ' + beautiful_time(time.time() - start))
    loges_file.close()
