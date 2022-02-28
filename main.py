import subprocess, os
from ares import FuckAres

print('Verifing module and Nuitka...')

try:
    __import__('rich')
    __import__('pystyle')
    
    if os.system("nuitka") != 0:
        print('Please install Nuitka ! ( pip install nuitka and require C++ )')
        exit(0)
except Exception as e:
    if "ModuleNotFoundError" in e:
        os.system("pip install rich pystyle")
        exit(0)
        
FuckAres()