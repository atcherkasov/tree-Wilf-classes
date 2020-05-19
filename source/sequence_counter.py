def sequence_num(directory_path: str):
    import os
    all_files = os.listdir(directory_path)
    different_series = set()
    for file_name in all_files:
        file = open(directory_path + '/' + file_name, 'r')
        series = file.readlines()[2]
        different_series.add(series)
    print(len(different_series))


if __name__ == '__main__':
    sequence_num('../output_files/Av_10_257')
