import os
import sys
sys.path.append(os.getcwd())

from source.get_series import beautiful_time
from source.sequence_evaluation import compute_sequence
from source.poly_func.my_poly_functions import show_local
from source.parsers import parser
from source import parallel_setup
import time


if __name__ == '__main__':
    args = sys.argv

    dots = ''

    try:
        leaf_number = int(args[1])
        x_len = int(args[2])
        start_fold = int(args[3])
        end_fold = int(args[4])
        free_proc = int(args[5])
        handle = args[6]
    except:
        print('You hae got un correct list of args')
        print('copy this example: ')
        print('\n\tpython3 source/Avoidance.py 9 65 0 1000 0 Sasha\n')
        exit(0)

    parallel_setup.init(free_proc)

    start = time.time()
    groups, leaf_number = parser(dots + 'input_files/equations_short_' + str(leaf_number) + '.txt')

    if start_fold > end_fold:
        change = -1
        start_fold = min(start_fold, len(groups))
    else:
        change = 1
        end_fold = min(end_fold, len(groups))

    out_dir_path = dots + 'output_files/Av_' + str(leaf_number) + '_' + str(x_len)
    try:
        os.mkdir(out_dir_path)
    except:
        pass

    log_dir_path = dots + 'loges/Av_' + str(leaf_number) + '_' + str(x_len)
    try:
        os.mkdir(log_dir_path)
    except:
        pass

    loges_file = open(log_dir_path + '/' + handle + '_from_' + str(min(start_fold, end_fold)) + '_to_' + str(max(start_fold, end_fold)) + '.txt', 'w')

    part = 2.5
    part_time = part

    already_counted_folds = set([int(file_name[:file_name.find('_')]) for file_name in os.listdir(out_dir_path)])
    indexes = set(range(start_fold, end_fold, change)) - already_counted_folds
    indexes = sorted(list(indexes))
    local_ind = -1
    for i in indexes:
        local_ind += 1
        lit_start = time.time()
        x_series = compute_sequence(groups[i][1:], (x_len + 1) // 2)
        file = open(out_dir_path + '/' + str(i) + '_fold_' + handle + '.txt', 'w')
        print(time.time() - lit_start, file=file)
        print(groups[i][0][:-1], file=file)
        print(show_local(x_series, loc='x'), file=file)

        percent = round(local_ind / float(len(indexes)) * 100, 1)
        if percent >= part_time:
            print('посчитанно', str(percent) + '%. За',
                  beautiful_time(time.time() - start), file=loges_file)
            print('посчитанно', str(percent) + '%. За',
                  beautiful_time(time.time() - start))

            part_time += part
        else:
            pass
            # print(percent, '%')
        file.close()

    print(' ВЕСЬ ПРОЦЕСС ЗАНЯЛ: ' + beautiful_time(time.time() - start),
          file=loges_file)
    print('заняло ' + beautiful_time(time.time() - start))
    loges_file.close()
