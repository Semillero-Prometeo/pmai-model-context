#https://psutil.readthedocs.io/stable/

import psutil
import os

def measure_process_cpu(interval=1):
    p = psutil.Process(os.getpid())
    return p.cpu_percent(interval=interval)
