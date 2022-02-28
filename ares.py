import subprocess
import time
import marshal

from os import system, path, mkdir, getcwd, remove
from sys import platform
from pathlib import Path
from shutil import rmtree, copy2

from pystyle import Colors, Colorate
from rich.console import Console

class FuckAres:
    
    def __init__(self):
        self.console = Console()
        self.logs = []
        self.basic_params = ["nuitka", "--mingw64", "--onefile", "main.py"]
        self.dist_folder = path.join(getcwd(), "dist")
        
        self.init_file = None
        self.use_icon = None
        self.folder_and_files = []
        self.parametres = {
            "hidden_console": {
                "value": False,
                "description": "Do you want the console to be hidden ?"
            },
            "admin_program": {
                "value": False,
                "description": "Do you want to run the program as administrator ?",
                "path": "resources/admin.py" 
            },
            "anti_vm": {
                "value": False,
                "description": "Do you want to block virtual machines ? (soon...)",
                "path": "resources/vm.py" 
            },
            "anti_debugger": {
                "value": False,
                "description": "Do you want to block the debugger ?",
                "path": "resources/debugger.py"   
            },
            "anti_network_traffic": {
                "value": False,
                "description": "Do you want to block the network traffic ?",
                "path": "resources/network.py" 
            },
            "anti_ctrl_c": {
                "value": False,
                "description": "Do you want to put an anti ctrl+c ?",
                "path": "resources/ctrl_c.py" 
            },
        }
        
        self.main()
        
    def title(self):
        system("clear" if platform == "nt" else "cls")
        bn = """

  _____           _    _                  _                  
 |  ___|   _  ___| | _(_)_ __   __ _     / \\   _ __ ___  ___ 
 | |_ | | | |/ __| |/ / | '_ \\ / _` |   / _ \\ | '__/ _ \\/ __|
 |  _|| |_| | (__|   <| | | | | (_| |  / ___ \\| | |  __/\\__ \\
 |_|   \\__,_|\\___|_|\\_\\_|_| |_|\\__, | /_/   \\_\\_|  \\___||___/
                               |___/                         
    
"""

        print(Colorate.Diagonal(Colors.blue_to_purple, bn))
        print(Colorate.Diagonal(Colors.red_to_blue, "   >>> You're a piece of shit venax."))
        print(Colorate.Diagonal(Colors.red_to_blue, "   >>> Fucking Ares by Bleu#7728"))
        print(Colorate.Diagonal(Colors.red_to_blue, "   >>> Source code on my GitHub @Bleu-No/Fuck-You-Ares"))
        
        if len(self.logs) > 0:
            print("\n")
            for value in self.logs:
                self.console.log(value)
    
    def verify_licence(self):
        self.title()
        while True:
            key = self.console.input("\nThe only fucking license there is Bleu#7728, okay? : ")
            if key != "Bleu#7728":
                print(Colorate.Diagonal(Colors.red_to_blue, "I said the only fucking license that exists is Bleu#7728 ! Are you stupid ?"))
            else:
                self.logs.append("Okay good licence.")
                break
    
    def enter_file_and_verify(self):
        self.title()
        while True:
            input_file = self.console.input("\nNow enter your Python file to compile [Example: hello.py]: ")
            if not path.exists(input_file):
                print(Colorate.Diagonal(Colors.red_to_blue, "You can't enter a file that exists ?"))
            elif Path(input_file).suffix != ".py":
                print(Colorate.Diagonal(Colors.red_to_blue, "Well... you have to enter a Python file in .py !"))
            else:
                self.init_file = input_file
                self.logs.append(f"Main file: {self.init_file}")
                break
            
    def add_extern_folder_or_file(self):
        self.title()
        choice = self.console.input("\nWant to add a folder or an external file ? (Y/N) (soon...): ")
        if choice.lower() == "y":
            self.title()
            temp_logs = []
            
            while True:
                input_file_or_folder = self.console.input("\nPlease enter the path of your folder or file (done -> stop): ")
                if str(input_file_or_folder) == "done":
                    break
                elif not path.exists(input_file_or_folder):
                    print(Colorate.Diagonal(Colors.red_to_blue, "The file or folder does not exist !"))
                elif input_file_or_folder in temp_logs:
                    print(Colorate.Diagonal(Colors.red_to_blue, "The file or folder has already been added to the list !"))
                elif input_file_or_folder == self.init_file:
                    print(Colorate.Diagonal(Colors.red_to_blue, "You cannot add the main file !"))
                else:
                    temp_logs.append(input_file_or_folder)
                    if Path(input_file_or_folder).is_dir():
                        print(Colorate.Diagonal(Colors.green_to_blue, "The folder has been added !"))
                        self.folder_and_files.append(["folder", input_file_or_folder])
                        self.logs.append(f"Add external file: {input_file_or_folder}")
                    else:
                        print(Colorate.Diagonal(Colors.green_to_blue, "The file has been added !"))
                        self.folder_and_files.append(["file", input_file_or_folder])
                        self.logs.append(f"Add external folder: {input_file_or_folder}")
        else:
            self.logs.append("No use external file or folder.")
    
    def add_icon(self):
        self.title()
        input_file = self.console.input("\nPlease enter the path of your icon [Example: hello.ico] (optional): ")
        if path.exists(input_file) and Path(input_file).suffix == ".ico":
            self.use_icon = input_file
            self.logs.append(f"Use icon: {input_file}")
        else:
            self.logs.append("No use icon.")
    
    def set_parametres(self):
        for value in self.parametres:
            self.title()
            input_params = self.console.input(f"\n{self.parametres[value]['description']} (Y/N): ")
            if input_params.lower() == "y":
                self.parametres[value]["value"] = True
            self.logs.append(f"Settings {value}: {self.parametres[value]['value']}")
    
    def cleaner(self):
        name_file = str(self.init_file).split('.')[0] + ".exe"
        
        if path.exists(name_file):
            remove(name_file)
    
        copy2("dist/main.exe", name_file);
        rmtree(self.dist_folder)
    
    def compilation(self):
        self.title()
        
        start = time.time()
        self.logs.append(f"Started compilation of {self.init_file}...")
        
        if path.exists(self.dist_folder):
          rmtree(self.dist_folder)
        mkdir(self.dist_folder)
        
        if self.parametres["hidden_console"]["value"]:
            self.basic_params.append("--windows-disable-console")
            
        if self.use_icon:
            self.basic_params.append("--windows-icon-from-ico=icon.ico")
            copy2(self.use_icon, "dist/icon.ico")
            
        content_file = open(self.init_file, "r").read()
        new_main_file = open("dist/main.py", "w")
        
        for value in self.parametres:
            if self.parametres[value]["value"]:
                if self.parametres[value]["path"] and path.exists(self.parametres[value]["path"]):
                    try:
                        source_file = open(self.parametres[value]["path"], "rb").read()
                        compile_source = marshal.dumps(compile(source_file, f"<frozen {value}>", "exec"))
                        
                        new_main_file.write(f"exec(__import__('marshal').loads({compile_source}));\n")
                    except:
                        self.logs.append(f"Fail to load {value} file in resources directory !")
                else:
                    self.logs.append(f"{value} file in resources is not found !")
        
        if self.parametres["anti_debugger"]["value"] or self.parametres["anti_network_traffic"]["value"]:
            self.basic_params.append("--include-module=psutil")
        
        new_main_file.write(f"\n\n{content_file}")
        new_main_file.close()
        
        self.title()
        
        print("\n")
        self.console.print(f"Compiling {self.init_file}...")
        p = subprocess.Popen(self.basic_params, stdout=subprocess.DEVNULL, shell=True, cwd=self.dist_folder)
        p.wait()
            
        ntime = str((time.time() - start)).split(".")[0]
        self.logs.append(f"Compiled in {ntime} seconds !")
            
        self.title()
        start = time.time()
        self.console.status("Cleaning...")
        self.cleaner()

        ntime = str((time.time() - start)).split(".")[0]
        self.logs.append(f"Cleaned in {ntime} seconds !")

        name_file = str(self.init_file).split('.')[0] + ".exe"
        size_file = str(len(open(name_file, "rb").read()) / 1000000).split(".")[0]
        
        self.logs.append(f"Output file: {path.join(getcwd(), name_file)}")
        self.logs.append(f"File size: {size_file}mb")
        
        self.title()
        
        print("\n")
        self.console.print("\nAnd that's it! And all this for free not for 30$ lol")
        
    
    def main(self):
        self.verify_licence()
        self.enter_file_and_verify()
        self.add_extern_folder_or_file()
        self.add_icon()
        self.set_parametres()
        self.compilation()