from pystyle import Colors, Colorate

def Banner():
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