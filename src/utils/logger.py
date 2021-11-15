from colorama import Fore, Back, Style
from pyfiglet import Figlet
import time
import sys

BOLD = '\033[1m'
EREASE = '\x1b[2K'
UP = '\x1b[1A'

def print_banner():
    f = Figlet(font='bulbhead')
    print(Fore.RED + f.renderText('Pixel') + Fore.BLUE + f.renderText('Police'))

def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)          

def erease_last_line():
    time.sleep(.1)
    sys.stdout.write(UP)
    sys.stdout.write(EREASE)




def print_running_message(message: str) -> None:
    print_with_color(f"{BOLD} INVESTIGATING ", color=Back.YELLOW + Fore.BLACK, brightness=Style.NORMAL, end="  ")
    print_with_color(message[0:message.rfind('/')], color=Fore.WHITE, brightness=Style.DIM, end="")
    print_with_color(message[message.rfind('/'):len(message)], color=Fore.WHITE, brightness=Style.BRIGHT)

def print_clean_message(message: str) -> None:
    erease_last_line()
    print_with_color(f"{BOLD} CLEAN ", color=Back.BLUE + Fore.BLACK, brightness=Style.NORMAL, end="  ")
    print_with_color(message[0:message.rfind('/')], color=Fore.WHITE, brightness=Style.DIM, end="")
    print_with_color(message[message.rfind('/'):len(message)], color=Fore.WHITE, brightness=Style.BRIGHT)

def print_dirty_message(message: str) -> None:
    erease_last_line()
    print_with_color(f"{BOLD} DIRTY ", color=Back.RED + Fore.BLACK, brightness=Style.NORMAL, end="  ")
    print_with_color(message[0:message.rfind('/')], color=Fore.WHITE, brightness=Style.DIM, end="")
    print_with_color(message[message.rfind('/'):len(message)], color=Fore.WHITE, brightness=Style.BRIGHT)
    
if __name__ == "__main__":
    print_banner()
    print_running_message("src/components/VehicleComparison.styles.tsx")
    time.sleep(3)
    print_clean_message("src/components/VehicleComparison.styles.tsx")
    print_running_message("src/components/VehicleOverview.styles.tsx")
    time.sleep(3)
    print_dirty_message("src/components/VehicleOverview.styles.tsx")
    print_running_message("src/components/VehicleCard.styles.tsx")
    time.sleep(1)
    print_dirty_message("src/components/VehicleCard.styles.tsx")

