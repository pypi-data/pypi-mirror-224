import time
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def timeIt(function):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        function(*args,**kwargs)
        end_time = time.time()
        completion_time = end_time-start_time
        print(Fore.BLUE + f"\nFunction: {Fore.GREEN +function.__name__} {Fore.RED}| {Fore.BLUE}RunTime: {Fore.GREEN + format(completion_time,'.8f')} sec {Fore.RED}|\n")
        print(Style.RESET_ALL)
    return wrapper
