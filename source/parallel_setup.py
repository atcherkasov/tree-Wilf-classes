def init(free_proc: int):
    from multiprocessing import Pool, cpu_count
    global pool
    pool = Pool(cpu_count() - free_proc)