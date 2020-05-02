def init(groups, file, loges_file, current):
    from multiprocessing import Pool, cpu_count
    global pool

    pool = Pool(cpu_count(), initializer, (groups, file, loges_file, current))


def initializer(_groups, _file, _loges_file, _current):
    global groups, file, loges_file, current
    groups = _groups
    file = _file
    loges_file = _loges_file
    current = _current
