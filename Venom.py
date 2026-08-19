import os
import ssl
import subprocess
try: 
    import certifi 
    os.environ.setdefault('SSL_CERT_FILE', certifi.where()) 
    os.environ.setdefault('REQUESTS_CA_BUNDLE', certifi.where()) 
except ImportError: 
    pass 
import requests, os, sys, re, time, os.path, ctypes, getpass 
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System 
from colorama import Fore 
from urllib.request import Request, urlopen 
import nextcord 
 
### COLORS AND VARS ### 
VERSIONETOOL = "0.0.1 [BETA]" 
c = Fore.LIGHTCYAN_EX 
g = Fore.LIGHTGREEN_EX 
y = Fore.LIGHTYELLOW_EX 
b = Fore.LIGHTBLUE_EX 
w = Fore.LIGHTWHITE_EX 
m = Fore.LIGHTMAGENTA_EX 
 
 
### SETUP DISCORD ### 
import nextcord 
from nextcord.errors import LoginFailure 
from nextcord.ext import commands 
from nextcord.utils import get 
intents = nextcord.Intents.default() 
intents.members = True 
intents.guild_messages = True  
intents.messages = True 
intents.guilds = True 
#nuker = commands.Bot(command_prefix=";",intents=intents) 
 
class Bot(commands.Bot): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
 
nuker = Bot() 
 
 
global statobot
statobot = 'Offline'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_FILES = {
    '1': 'Ban all.py',
    '2': 'Delete Channels.py',
    '3': 'Delete Roles.py',
    '4': 'Modify Everyone.py',
    '5': 'Create Channels.py',
    '6': 'Change Server Name.py',
    '7': 'Delete emojis.py',
}


def data_file(name):
    return os.path.join(BASE_DIR, name)


def read_setting(name):
    try:
        with open(data_file(name), "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def write_setting(name, value):
    with open(data_file(name), "w", encoding="utf-8") as f:
        f.write(str(value).strip())


def resolve_script_path(option):
    filename = SCRIPT_FILES.get(str(option))
    if not filename:
        return None
    scripts_dir = os.path.join(BASE_DIR, 'scripts')
    for name in os.listdir(scripts_dir):
        if name.lower() == filename.lower():
            return os.path.join(scripts_dir, name)
    return None


def run_script_option(option):
    script_path = resolve_script_path(option)
    if script_path is None:
        return False
    subprocess.run([sys.executable, script_path], check=False)
    return True

### SCREEN ###
def impostatitolo(_str):
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
 
def titolohome(): 
#    print(f"""\n\n 
#                ╭━╮╱╭┳╮╱╭┳╮╭━┳━━━┳━━━╮╭━━━━┳━━━┳━━━┳╮ 
#                ┃┃╰╮┃┃┃╱┃┃┃┃╭┫╭━━┫╭━╮┃┃╭╮╭╮┃╭━╮┃╭━╮┃┃ 
#                ┃╭╮╰╯┃┃╱┃┃╰╯╯┃╰━━┫╰━╯┃╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃ 
#                ┃┃╰╮┃┃┃╱┃┃╭╮┃┃╭━━┫╭╮╭╯╱╱┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮ 
#                ┃┃╱┃┃┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮╱╱┃┃╱┃╰━╯┃╰━╯┃╰━╯┃ 
#                ╰╯╱╰━┻━━━┻╯╰━┻━━━┻╯╰━╯╱╱╰╯╱╰━━━┻━━━┻━━━╯    
#\n""".replace('█', f'{g}█{y}')) 
    print(f"""\n\n 
 
███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗ 
██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝ 
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗ 
██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║ 
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
 
████████╗ ██████╗  ██████╗ ██╗      
╚══██╔══╝██╔═══██╗██╔═══██╗██║      
   ██║   ██║   ██║██║   ██║██║      
   ██║   ██║   ██║██║   ██║██║      
   ██║   ╚██████╔╝╚██████╔╝███████╗ 
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ 
 
\n""".replace('█', f'{g}█{y}')) 
 
banner = r""" 
██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗ 
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║ 
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║ 
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║ 
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║ 
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ 
 
""" [1:] 
 
def transizione(): 
    clear() 
    caricamento() 
    clear() 
 
def caricamento(): 
    carattere = ['|', '/', '-', '\\'] 
    for i in carattere+carattere+carattere: 
        sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""") 
        sys.stdout.flush() 
        time.sleep(0.2) 
 
@nuker.event 
async def on_ready(): 
    global statobot 
    statobot = 'Online' 
    print("Bot logged in:") 
    print("ID: " + str(nuker.user.id)) 
    print("Name: " + str(nuker.user.name)) 
    main() 
 
from scripts import * 
def main(): 
    impostatitolo(f"Mat Nuker Tool {VERSIONETOOL} - Loading") 
    System.Size(160, 40) #120, 30 
    Anime.Fade(Center.Center(banner), Colors.green_to_red, Colorate.Vertical, time=1) 
    clear() 
    token = '' if read_setting('token.txt') else 'Not Found'
    server = read_setting('server.txt') or 'Not Found'
    global statobot 
    impostatitolo(f"Mat Nuker Tool {VERSIONETOOL}") 
    titolohome() 
    print(f"""      
          {y}[{b}+{y}]{g} Main:                              {y}[{b}+{y}]{c} Settings: 
          {y}[{w}1{y}]{g} Ban all members                    {y}[{w}10{y}]{c} Set bot token 
          {y}[{w}2{y}]{g} Delete all channels                {y}[{w}11{y}]{c} Set server ID to grief               
          {y}[{w}3{y}]{g} Delete all roles                   {y}[{w}12{y}]{c} Start bot  
          {y}[{w}4{y}]{g} Give @everyone administrator 
          {y}[{w}5{y}]{g} Create channels 
          {y}[{w}6{y}]{g} Change server name 
          {y}[{w}7{y}]{g} Delete server emojis 
 
          {m}Modify by abidhsajid 
          {m}Token:{b}{token} 
          {m}Server    : {b}{server} 
          {m}Bot Status : {b}{statobot}                                                                       
\t\t\t\t\t\t\t\t\t\t\t\t\t""") 
    global scelta 
    scelta = input(f"""{y}[{b}#{y}]{w} [{getpass.getuser()}]: """) 
    if scelta == '1' or scelta == '01': 
        if statobot == 'Online': 
            server = read_setting('server.txt')
            if not server:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
            try:
                serverr = nuker.get_guild(int(server))
                run_script_option(1)
            except (FileNotFoundError, ValueError):
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
        else: 
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Start the bot first [option 12 in home]!") 
            main() 
            return
    elif scelta == '2' or scelta == '02': 
        if statobot == 'Online': 
            server = read_setting('server.txt')
            if not server:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
            try:
                serverr = nuker.get_guild(int(server))
                run_script_option(2)
            except (FileNotFoundError, ValueError):
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
        else: 
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Start the bot first [option 12 in home]!") 
            main() 
            return
    elif scelta == '3' or scelta == '03': 
        if statobot == 'Online': 
            server = read_setting('server.txt')
            if not server:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
            try:
                serverr = nuker.get_guild(int(server))
                run_script_option(3)
            except (FileNotFoundError, ValueError):
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
        else: 
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Start the bot first [option 12 in home]!") 
            main() 
            return
    elif scelta == '4' or scelta == '04': 
        if statobot == 'Online': 
            server = read_setting('server.txt')
            if not server:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
            try:
                serverr = nuker.get_guild(int(server))
                run_script_option(4)
            except (FileNotFoundError, ValueError):
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
        else: 
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Start the bot first [option 12 in home]!") 
            main() 
            return
    elif scelta == '5' or scelta == '05': 
        if statobot == 'Online': 
            server = read_setting('server.txt')
            if not server:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
            try:
                serverr = nuker.get_guild(int(server))
                run_script_option(5)
            except (FileNotFoundError, ValueError):
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
        else: 
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Start the bot first [option 12 in home]!") 
            main() 
            return
    elif scelta == '6' or scelta == '06': 
        if statobot == 'Online': 
            server = read_setting('server.txt')
            if not server:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
            try:
                serverr = nuker.get_guild(int(server))
                run_script_option(6)
            except (FileNotFoundError, ValueError):
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
        else: 
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Start the bot first [option 12 in home]!") 
            main() 
            return
    elif scelta == '7' or scelta == '07': 
        if statobot == 'Online': 
            server = read_setting('server.txt')
            if not server:
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
            try:
                serverr = nuker.get_guild(int(server))
                run_script_option(7)
            except (FileNotFoundError, ValueError):
                input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Missing Server ID [option 11 in home]!")
                main()
                return
        else: 
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} Start the bot first [option 12 in home]!") 
            main() 
            return
    elif scelta == '10' or scelta == '010': 
        transizione() 
        diocane = input(f'{y}[{b}#{y}]{w} Enter the bot token:    ')
        write_setting('token.txt', diocane)
        main() 
    elif scelta == '11' or scelta == '011': 
        transizione() 
        diocane = input(f'''{y}[{b}#{y}]{w} Enter the ID of the server to target:    ''')
        write_setting('server.txt', diocane)
        main() 
    elif scelta == '12' or scelta == '012': 
        transizione()
        token = read_setting('token.txt')
        server = read_setting('server.txt')
        if not token or not server:
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} You must set the bot token and server ID first!")
            main()
            return
        try:
            nuker.run(token)
        except (LoginFailure, ssl.SSLCertVerificationError, requests.exceptions.SSLError, OSError, ValueError):
            input(f"{y}[{Fore.LIGHTRED_EX }!{y}]{w} The entered token is invalid!")
            main()
            return
    elif scelta == 'exit' or scelta == 'chiudi': 
        transizione() 
        sys.exit() 
    else: 
        clear() 
        main() 
 
 
 
 
if __name__ == "__main__": 
    main()