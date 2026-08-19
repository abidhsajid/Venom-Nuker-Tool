import os, os.path
from colorama import Fore
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

VERSIONETOOL = "0.0.1 [BETA]"
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
m = Fore.LIGHTMAGENTA_EX

### SCREEN ###
def set_title(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | github.com/abidhsajid")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} | github.com/abidhsajid\x07")
    else:
        pass

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def home_title():
    print(f"""\n\n
                ╭━╮╱╭┳╮╱╭┳╮╭━┳━━━┳━━━╮╭━━━━┳━━━┳━━━┳╮
                ┃┃╰╮┃┃┃╱┃┃┃┃╭┫╭━━┫╭━╮┃┃╭╮╭╮┃╭━╮┃╭━╮┃┃
                ┃╭╮╰╯┃┃╱┃┃╰╯╯┃╰━━┫╰━╯┃╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃
                ┃┃╰╮┃┃┃╱┃┃╭╮┃┃╭━━┫╭╮╭╯╱╱┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮
                ┃┃╱┃┃┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮╱╱┃┃╱┃╰━╯┃╰━╯┃╰━╯┃
                ╰╯╱╰━┻━━━┻╯╰━┻━━━┻╯╰━╯╱╱╰╯╱╰━━━┻━━━┻━━━╯   
\n""".replace('█', f'{g}█{y}'))

banner = r"""
██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝

""" [1:]

def transition():
    clear()
    Spinner()
    clear()

def Spinner():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
        sys.stdout.flush()
        time.sleep(0.2)