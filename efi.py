import random
import os
import sys
import time
import requests

from colorama import init, Fore, Style

from pyfiglet import Figlet



def printg(text):
    init()
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")

def create_ascii_art(text, font="standard"):
    fig = Figlet(font=font)
    ascii_art = fig.renderText(text)
    printg(ascii_art)
    
create_ascii_art("EFI     by Aesthetic")
printg("")
printg("Version 1.7")
print(" ")

def animated_loading(seconds):
    start_time = time.time()
    animation = "|/-\\"
    idx = 0

    while time.time() - start_time < seconds:
        sys.stdout.write("\r" + "Registering EFI " + animation[idx % len(animation)])
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    print(" ")
    print(" ")
    sys.stdout.write("\r" + "EFI has been successfully registered in the system!    \n")

def randomize_15_chars(input_str):
    space_index = input_str.find(" ", input_str.find("/")+3)

    if space_index != -1:
        suffix = input_str[space_index+1:]
        if len(suffix) >= 15:
            randomized_chars = ''.join(random.sample(suffix[:15], 15))
            result = input_str[:space_index+1] + randomized_chars + input_str[space_index+16:]
            return result
    return input_str

def process_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as input_file:
            content = input_file.readlines()

        for i in range(len(content)):
            if content[i].startswith("AMIDEEFIx64.efi /"):
                content[i] = randomize_15_chars(content[i])

        with open(output_file_path, 'w') as output_file:
            output_file.writelines(content)

    except FileNotFoundError:
        print("Error: Put the loader inside the USB along with EFI files.")
        input("Press enter to continue...")
        sys.exit()

url = "https://raw.githubusercontent.com/zzsjnvts/myraw/main/efi.txt"
search_string = input("Enter your key:")
print("")

if not search_string.strip():
    print("Invalid Key! please contact Aesthetic.")
    input("Press enter to exit....")
    sys.exit()

try:
    response = requests.get(url)
    response.raise_for_status() 
    if search_string in response.text:
        print("Logged in successfully.")
        print(" ")
    else:
        print("Invalid key, please contact Aesthetic.")
        input("Press enter to exit....")
        sys.exit()

except requests.exceptions.RequestException as e:
    print("Error occured.")
    
input_file_path = "Startup.nsh"
output_file_path = "Startup.nsh"

process_file(input_file_path, output_file_path)

directory_path = 'efi\\boot'
file_path = os.path.join(directory_path, 'startup.nsh')

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    output_file_path = "efi\\boot\\startup.nsh"
    process_file(input_file_path, output_file_path)

loading_time = 5
animated_loading(loading_time)

input("Press enter to exit..")
