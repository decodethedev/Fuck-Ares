from psutil import process_iter
from time import sleep
from threading import Thread

def anti_debugger():
    name_process = ["x32dbg", "x64dbg", "x96dbg", "IDA", "ProcessHacker"]
    
    while True:
        for process in process_iter():
            for name in name_process:
                if name.lower() in process.name().lower():
                    process.kill()
        sleep(0.10)
        
Thread(target=anti_debugger, args=()).start()