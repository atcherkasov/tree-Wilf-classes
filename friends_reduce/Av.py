import os
import sys
sys.path.append(os.getcwd())


from threading import Thread, Timer
from subprocess import Popen, PIPE
from typing import IO
from typing import *

# Хук для логгинга в дискорд
ds_file = open('friends_reduce/ds_webhook.txt', 'r')
WEBHOOK_URL = ds_file.readline()
# Скрипт таски. PYTHONPATH автоматически прокидывается равным CWD
TASK_SCRIPT = 'source/Avoidance.py'

# Аргументы запуска джоба. Первые четыре числа можно попросить у @chat_22, остальные
# два аргумента - число СВОБОДНЫХ (!!!) процессов и ник воркера соответственно.
args = sys.argv
try:
    leaf_number = int(args[1])
    x_len = int(args[2])
    start_fold = int(args[3])
    end_fold = int(args[4])
    free_proc = int(args[5])
    handle = args[6]
    frequency_flag = 'f'
    if len(args) > 7:
        frequency_flag = args[7]
except:
    print('You hae got un correct list of args')
    print('copy this example: ')
    print('\n\tpypy3 friends_reduce/Av.py 9 65 0 1000 0 Sasha\n')
    exit(0)

TASK_ARGUMENTS = leaf_number, x_len, start_fold, end_fold, free_proc, handle, frequency_flag


class Batya:
    def __init__(self):
        self.pipe = self.prepare_pipe()
        self.terminated = False
        self.out_thread = self.err_thread = None
        self.hook = Webhook.from_url(WEBHOOK_URL, adapter=RequestsWebhookAdapter())

    def prepare_pipe(self) -> Popen:
        cmd = [sys.executable, '-u', TASK_SCRIPT] + list(map(str, TASK_ARGUMENTS))
        pipe = Popen(
            cmd,
            stdout=PIPE,
            stderr=PIPE,
            shell=False,
            bufsize=0,
            universal_newlines=True,
            env={**os.environ, 'PYTHONPATH': str(os.getcwd())},
        )
        return pipe

    def flush(self, buffer: List[str], callback: Callable[[str], None]):
        result = ''.join(buffer)
        buffer.clear()
        callback(result)

    def fetch(self, target: IO, callback: Callable[[str], None]):
        buffer = []
        timer = None
        while not self.terminated:
            chunk = target.read(1)
            if not chunk: return
            buffer.append(chunk)
            if timer is None or not timer.is_alive():
                timer = Timer(interval=1, function=self.flush, args=(buffer, callback))
                timer.start()

    def log(self, buffer: str):
        self.hook.send(
            content=f'```{buffer}```',
            wait=False,
            username=f'[{handle}] Friend',
        )

    def run(self):
        self.log(f'<<< STARTING Friend WITH ARGS: {TASK_ARGUMENTS} >>>')
        self.out_thread = Thread(target=self.fetch, args=(self.pipe.stdout, self.log))
        self.err_thread = Thread(target=self.fetch, args=(self.pipe.stderr, self.log))
        self.out_thread.start()
        self.err_thread.start()
        self.pipe.wait()
        self.terminated = True
        self.out_thread.join()
        self.err_thread.join()
        self.log('<<< Friend TERMINATED >>>')


if __name__ == '__main__':
    if WEBHOOK_URL == '':
        cmd = "pypy3 " + TASK_SCRIPT + " " + " ".join(list(map(str, TASK_ARGUMENTS)))
        os.system(cmd)
    else:
        from discord import Webhook, RequestsWebhookAdapter
        batya = Batya()
        batya.run()
