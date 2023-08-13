import os


def read_files_as_strings():
    file_string = " #include <cuda_runtime.h> \n "
    current_directory = os.getcwd()
    print(os.listdir(current_directory))
    for dirpath, _, filenames in os.walk(current_directory+"/pycuga/algos/cuda/"):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, 'r') as file:
                file_string+= file.read()
            file_string+="\n"
    return file_string