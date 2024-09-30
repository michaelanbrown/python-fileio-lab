def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:

def read_file(file_name):
    pass
