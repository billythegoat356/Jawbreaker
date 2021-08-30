# -*- coding: utf-8 -*-


# GLOBALS DICT

from base64 import b16encode, b32encode, b64encode, b16decode, b32decode, b64decode
from builtins import *

globals_names = {k:v for k,v in globals().items()}


# REQUIREMENTS

from pyfade import Colors, Fade
from pycenter import center
from requests import get, post

from random import randint, choice
from os.path import isfile
from os import name, system


def clear():
    system("cls" if name == 'nt' else "clear")

clear()



if name == 'nt':
    system("title Jawbreaker")
    system("mode 160, 40")

encoding = 'utf-8'
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ignore = ("b16encode", "b32encode", "b64encode")


class Col:
    colors = {"red" : "\033[38;2;255;0;0m", 
              "gray" : "\033[38;2;150;150;150m", 
              "darkgray" : "\033[38;2;100;100;100m", 
              "white" : "\033[38;2;255;255;255m"}

    red = colors['red']

    gray = colors['gray']

    darkgray = colors['darkgray']

    white = colors['white']

        
    def printf(text):
        print(Col.darkgray + text)




class Create():
        def __init__(self):
            self.content= ""
        def write(self, content):
            self.content += content






jawbreaker = """
       #                                                                
       #   ##   #    # #####  #####  ######   ##   #    # ###### #####  
       #  #  #  #    # #    # #    # #       #  #  #   #  #      #    # 
       # #    # #    # #####  #    # #####  #    # ####   #####  #    # 
 #     # ###### # ## # #    # #####  #      ###### #  #   #      #####  
 #     # #    # ##  ## #    # #   #  #      #    # #   #  #      #   #  
  #####  #    # #    # #####  #    # ###### #    # #    # ###### #    # 
                                                                        
"""

author = "  # # # {} # # #".format(b64decode("YmlsbHl0aGVnb2F0MzU2").decode('utf-8'))

print(Fade.Vertical(Colors.white_to_black, center(jawbreaker)))
print(Fade.Horizontal(Colors.black_to_white, center(author)))

print("\n")

service = "https://Jawbreaker.billythegoat356.repl.co"

file = input(Col.gray+"Enter file name > "+Col.white)

if not isfile(file):
    print()
    input(Col.red+"This file doesn't exists!"+Col.white)
    exit()

output = input(Col.gray+"Enter name of output file > "+Col.white)
if not output and not isfile("new.py"):
    output = "new.py"




print()
Col.printf("\nBuilding obfuscated file...\n")

defined = []

def nfile(file:object, only:bool=False) -> tuple:
    
    temp_names = ["exec", "b16decode", "b32decode", "b64decode"] if only else [name for name in globals_names]

    Col.printf("Defining globals variables...")

    for name in temp_names:
        random_name = random()
        if name == "exec":
            exc = random_name = "sha256"
        elif name == "b16decode":
            b16 = random_name = "hash"
            file.write(f"from base64 import b16decode as {random_name};")
            b16 = random_name
            continue
        elif name == "b32decode":
            b32 = random_name = "b16"
            file.write(f"from base64 import b32decode as {random_name};")
            continue
        elif name == "b64decode":
            b64 = random_name = "xor"
            file.write(f"from base64 import b64decode as {random_name};")
            continue
        elif name in ignore:
            continue
        file.write(f"{random_name}={name};")
    return exc, b16, b32, b64

def random(l:int=2) -> str:
    while True:
        rdm = "".join(choice(chars) + choice([choice(chars), str(randint(0,9))]) for _ in range(1, l+1))
        if rdm not in defined:
            defined.append(rdm)
            return rdm
    

def build():

    with open(file, 'r', encoding=encoding) as f:
        content = f.read()

    Col.printf("Creating hastebin with https://github.com/billythegoat356/Raven...")
    content = "# obfuscated with https://github.com/billthegoat356/Jawbreaker\n\n# by billythegoat356\n\n# <3\n\n\n" + content

    try:
        response = post(service + "/create", data=content.encode('utf-8'),
                        headers={"Bypass-Tunnel-Reminder": "yea"})

        if response.status_code == 404:
            input(Col.red+"Error! Hastebin service is maybe down."+Col.white)
            exit()
    except:
        input(Col.red+"Error! Hastebin service is maybe down."+Col.white)
        exit()
        
    url = service + "/get/" + response.text
    Col.printf(f"Hastebin created! Url: {url}.")


    file_1 = Create()

    exc, b16, b32, b64 = nfile(file_1)

    urlp = random()
    req = random()

    Col.printf("Importing HTTP requests lib...")
    file_1.write(f"from urllib.request import urlopen as {urlp}, Request as {req};")

    chars_list = random()
    Col.printf("Creating content list...")
    file_1.write(f"{chars_list}=[];")
    content = f"""{exc}({urlp}({req}("{url}",headers={{"user-agent":"a"}})).read())"""

    Col.printf("Encoding content...")
    content = b16encode(b32encode(b64encode(content.encode(encoding)))).decode(encoding)

    random_chars_list = []

    Col.printf("Building content list...")

    for char in content:
        random_char = random()
        random_chars_list.append(random_char)
        file_1.write(f"{random_char}='{char}';")

    random_append_function = random()
    file_1.write(f"{random_append_function}={chars_list}.append;")

    for random_char in random_chars_list:
        file_1.write(f"{random_append_function}({random_char});")

    content_name = random()
    Col.printf("Creating variable to be desobfuscated...")
    file_1.write(f"{content_name} = ''.join({chars_list});")

    Col.printf("Building desobfuscator...")
    file_1.write(f"{exc}({b64}({b32}({b16}({content_name}))));")



    content = file_1.content
    
    content = b16encode(b32encode(b64encode(content.encode(encoding)))).decode(encoding)


    file_2 = Create()


    exc, b16, b32, b64 = nfile(file_2)


    Col.printf("Building second desobfuscator...")



    file_2.write(f'{exc}({b64}({b32}({b16}("{content}"))));')

    Col.printf("\nCreating final content...")
    content = file_2.content

    Col.printf("Writing content...")

    with open(output, 'w', encoding=encoding) as f:
        f.write(content)



try:
    build()
    print("\n")
    input(Col.gray+"Done!"+Col.white)
except Exception as e:
    input(Col.red+"Error! [{}]".format(e)+Col.white)
