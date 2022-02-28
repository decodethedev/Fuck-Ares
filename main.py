import subprocess
import time
import marshal

from os import system, path, mkdir, getcwd, remove
from sys import platform
from pathlib import Path
from shutil import rmtree, copy2

from pystyle import Write, Colors, Colorate
from resources.banner import Banner

folder_and_files = []
file = None
icon = None

hidden_console = None
anti_debugger = None
anti_network_traffic = None
anti_ctrl_c = None
anti_virtual_machine = None
admin_program = None

def title():
    clear()
    Banner()

def clear():
    system("clear" if platform == "nt" else "cls")

def licence():
    __key = Write.Input("\nThe only fucking license there is Bleu#7728 -> ", Colors.blue_to_purple, interval=0.001)
    if __key != "Bleu#7728":
        print(Colorate.Diagonal(Colors.red_to_blue, "I said the only fucking license that exists is Bleu#7728"))
        licence()

def file_enter():
    __file = Write.Input("\nNow enter your Python file to compile -> ", Colors.blue_to_purple, interval=0.001)
    
    if not path.exists(__file):
        print(Colorate.Diagonal(Colors.red_to_blue, "You can't enter a file that exists ?"))
        file_enter()
        
    if Path(__file).suffix != ".py":
        print(Colorate.Diagonal(Colors.red_to_blue, "Well... you have to enter a Python file in .py !"))
        file_enter()
    
    globals()['file'] = __file
        
def add_folder_and_file():
    __add = Write.Input("\nWant to add a folder or an external file ? (Y/N) -> ", Colors.blue_to_purple, interval=0.001)
    
    if __add.lower() == "n":
        return False
    else:
        
        def fuck():
            __add  = Write.Input("\nPlease enter the path of your folder or file (done -> stop) -> ", Colors.blue_to_purple, interval=0.001)
            
            if str(__add) == "done":
                return False
            elif not path.exists(__add):
                print(Colorate.Diagonal(Colors.red_to_blue, "The file or folder does not exist !"))
                fuck()
            elif __add in globals()['folder_and_files']:
                print(Colorate.Diagonal(Colors.red_to_blue, "The file or folder has already been added to the list !"))
                fuck()
            elif __add == globals()['file']:
                print(Colorate.Diagonal(Colors.red_to_blue, "You cannot add the main file !"))
                fuck()
            else:
                print(Colorate.Diagonal(Colors.green_to_blue, "The file or folder has been added !"))
                globals()['folder_and_files'].append(__add)
                fuck()

        title()
        fuck()
        
def use_icon():
    __icon = Write.Input("\nPlease enter the path of your icon (Example: hello.ico) (done -> no icon) -> ", Colors.blue_to_purple, interval=0.001)

    if str(__icon) == "done":
        return False
    elif not path.exists(__icon):
        print(Colorate.Diagonal(Colors.red_to_blue, "The file or folder does not exist !"))
        use_icon()
    elif Path(__icon).suffix != ".ico":
        print(Colorate.Diagonal(Colors.red_to_blue, "You must put a file with the extension .ico !"))
        use_icon()
    else:
        globals()['icon'] = __icon

def params():
    question = [
        ["hidden_console", "Do you want the console to be hidden ?"],
        ["anti_debugger", "Do you want to block the debugger ?"],
        ["anti_network_traffic", "Do you want to block the network traffic ?"],
        ["anti_ctrl_c", "Do you want to put an anti ctrl+c ?"],
        ["anti_virtual_machine", "Do you want to block virtual machines ?"],
        ["admin_program", "Do you want to run the program as administrator ?"]
    ]
    
    for qsk in question:
        def question(qsk):
            __qsk = Write.Input("\n" + qsk[1] + " -> ", Colors.blue_to_purple, interval=0.001)
        
            if __qsk.lower() == "y":
                globals()[qsk[0]] = True
            elif __qsk.lower() != "n":
                print(Colorate.Diagonal(Colors.red_to_blue, "You just have to answer with Y or N !"))
                question(qsk)
        title()
        question(qsk)

def compilation():
    start = time.time()
    
    print(Colorate.Diagonal(Colors.blue_to_purple, "\nCompiling your program..."))
    
    if path.exists('dist'):
          rmtree('dist')
    mkdir('dist')
    
    paramss = ["nuitka", "--mingw64", "--onefile", "--follow-imports"]
    
    content = open(globals()['file'], 'r').read()
    r = open('dist/main_program.py', 'w')
    
    if globals()['admin_program']:
        r.write(f"exec(__import__('marshal').loads({marshal.dumps(compile(open('resources/admin.py', 'rb').read(), '<main>', 'exec'))}))\n")
    
    if globals()['anti_ctrl_c']:
        r.write(f"exec(__import__('marshal').loads({marshal.dumps(compile(open('resources/anti_ctrl_c.py', 'rb').read(), '<main>', 'exec'))}))\n")
        
    r.write('\n\n\n')
    r.write(content)
    r.close()
    
    if globals()['icon']:
        paramss.append(f"--windows-icon-from-ico=icon.ico")
        copy2(globals()['icon'], "dist/icon.ico")
    if globals()['hidden_console']:
        paramss.append("--windows-disable-console")
        
    paramss.append("main_program.py")
    
    p = subprocess.Popen(paramss, shell=True, cwd=path.join(getcwd(), "dist"))
    p.wait()
    
    print(Colorate.Diagonal(Colors.blue_to_purple, "\nCleaning..."))
    
    size = str(len(open("dist/main_program.exe", "rb").read()) / 1000000).split(".")[0]
    
    if path.exists(f"{str(globals()['file']).split('.')[0]}.exe"):
        remove(f"{str(globals()['file']).split('.')[0]}.exe")
    
    copy2("dist/main_program.exe", f"{str(globals()['file']).split('.')[0]}.exe");
    rmtree("dist")
    
    title()
    
    ntime = str((time.time() - start)).split(".")[0]
    print(Colorate.Diagonal(Colors.blue_to_green, f"\nYour program has been compiled !\nSave path: {path.join(getcwd(), str(globals()['file']).split('.')[0]) + '.exe'}\nFile size: {size}mb\nTime: {ntime}s"))

if __name__ == "__main__":
    #verify licence
    title()
    licence()
    
    #enter file
    title()
    file_enter()
    
    #add file or folder
    title()
    add_folder_and_file()
    
    #add icon
    title()
    use_icon()
    
    #params
    title()
    params()
    
    #compilation
    title()
    compilation()