def sequence_num(directory_path: str):
    import os
    all_files = os.listdir(directory_path)
    different_series = set()
    for file_name in all_files:
        file = open(directory_path + '/' + file_name, 'r')
        series = file.readlines()[1]
        different_series.add(series)
    print(len(different_series))


if __name__ == '__main__':
    sequence_num('../rubbish_files/output_8_75')
    # hyp_test('output_files/long_data/series_8_111.txt')
    # hyp_test('rubbish_files/short_nice_series_10_13.txt')
