def init(free_proc: int, part_time, part, indexes, FREQUENCY_FLAG, start):
    from multiprocessing import Pool, cpu_count
    global pool

    pool = Pool(cpu_count() - free_proc, initializer, (part_time, part, indexes, FREQUENCY_FLAG, start))


def initializer(_part_time, _part, _indexes, _FREQUENCY_FLAG, _start):
    global part_time, part, indexes, FREQUENCY_FLAG, start
    part = _part
    part_time = _part_time
    indexes = _indexes
    FREQUENCY_FLAG = _FREQUENCY_FLAG
    start = _start
