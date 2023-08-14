# DataSystem.py
import platform
import os
import socket
from datetime import datetime
import psutil
import cpuinfo

def get_system_info():
    system_model = platform.system()
    
    ram_bytes = psutil.virtual_memory().total
    ram_gb = ram_bytes / (1024 ** 3)
    
    processor_info = platform.processor()
    
    try:
        import GPUtil
        gpu_info = GPUtil.getGPUs()[0].name
    except ImportError:
        gpu_info = "N/A"
    
    ip_address = socket.gethostbyname(socket.gethostname())
    
    user_name = os.getlogin()
    
    os_version = platform.release()
    
    python_version = platform.python_version()
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cpu_info = cpuinfo.get_cpu_info()
    cpu_count = psutil.cpu_count(logical=False)
    cpu_generation = cpu_info.get('brand_raw')
    
    system_info = {
        "System Model": system_model,
        "RAM (GB)": ram_gb,
        "Processor": processor_info,
        "GPU": gpu_info,
        "IP Address": ip_address,
        "User Name": user_name,
        "OS Version": os_version,
        "Python Version": python_version,
        "Current Time": current_time,
        "CPU Count": cpu_count,
        "CPU Generation": cpu_generation
    }
    
    return system_info
