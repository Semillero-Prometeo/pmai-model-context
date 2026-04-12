import timeit
from utils.model import model
import time

def medir_latencia(model):
    start_time = timeit.default_timer()
    latencia = model()
    end_time = timeit.default_timer()
    latencia = end_time - start_time
    
    return latencia