import random
import os
import sys
import time
print("EFI by Aesthetic")
print(" ")
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
    with open(input_file_path, 'r') as input_file:
        content = input_file.readlines()

    for i in range(len(content)):
        if content[i].startswith("AMIDEEFIx64.efi /"):
            content[i] = randomize_15_chars(content[i])

    with open(output_file_path, 'w') as output_file:
        output_file.writelines(content)

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
    



