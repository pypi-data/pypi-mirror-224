import subprocess
import time
import asciichartpy
import platform

def get_gpu_used_memory():
    output = subprocess.check_output(['nvidia-smi', '--query-gpu=memory.used', '--format=csv,nounits'])
    output = output.decode('utf-8')
    lines = output.strip().split('\n')
    used_memory = int(lines[1])
    return used_memory

def get_gpu_total_memory():
    output = subprocess.check_output(['nvidia-smi', '--query-gpu=memory.total', '--format=csv,nounits'])
    output = output.decode('utf-8')
    lines = output.strip().split('\n')
    total_memory = int(lines[1])
    return total_memory

def draw_gpu_memory(gpu_memory_history):
    used_memory = get_gpu_used_memory()
    total_memory = get_gpu_total_memory()

    used_percentage = used_memory / total_memory * 100
    gpu_memory_history.append(used_percentage)

    # 绘制字符图表
    chart = asciichartpy.plot(gpu_memory_history, {'height': 20, 'width': 10, 'timestamp': True})
    
    # 清空终端屏幕
    if platform.system() == 'Windows':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)
    
    print(chart)

def show_gpu_memory():
    while True:
        try:
            gpu_memory_history = []
            while True:
                draw_gpu_memory(gpu_memory_history)
                time.sleep(1)
        except KeyboardInterrupt:
            break
        
show_gpu_memory()