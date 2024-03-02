import random

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
output_file_path = "output.nsh"
process_file(input_file_path, output_file_path)


