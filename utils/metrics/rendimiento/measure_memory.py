import psutil
import psutil
def measure_memory():
    return psutil.virtual_memory().used / (1024 ** 3)

