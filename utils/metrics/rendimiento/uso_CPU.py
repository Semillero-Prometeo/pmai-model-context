import psutil
import time


def medir_uso_cpu():
    """
    Mide el uso de CPU por núcleo durante un período de tiempo determinado. Este método proporciona información detallada sobre la carga de trabajo en cada núcleo del procesador, lo que puede ser útil para identificar cuellos de botella y optimizar el rendimiento del modelo.
    """
    
    print("Monitoreando CPU por núcleo...")
    for i in range(3):

        uso_por_nucleo = psutil.cpu_percent(interval=1, percpu=True)
        
        print(f"Uso por núcleo: {uso_por_nucleo}")

        
        for idx, porcentaje in enumerate(uso_por_nucleo):
            print(f"  Núcleo {idx}: {porcentaje}%")
        print("-" * 20)
        time.sleep(1)  
        
    return uso_por_nucleo
