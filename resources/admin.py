import ctypes

def check_if_admin_mode():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not is_admin:
        print("Fuck Ares (Github @Bleu-No): Please run the program as administrator.")
        exit(0)
        
check_if_admin_mode()