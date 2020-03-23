def init():
    from multiprocessing import Pool, cpu_count
    global pool
    pool = Pool(cpu_count())