#!/usr/bin/python3

import sys
import os

import pefile


# Reference: https://docs.microsoft.com/en-us/windows/win32/debug/pe-format?redirectedfrom=MSDN#section-table-section-headers
EXECUTABLE_SECTION = 0x20000000


def isExecutable(section):
    characteristics = getattr(section, 'Characteristics')
    if characteristics & EXECUTABLE_SECTION > 0:
        return True

    return False


def getExecutables(file_path):
    pe = pefile.PE(file_path)

    executables = list([])
    for section in pe.sections:
        if isExecutable(section):
            executables.append(section.Name.decode("utf-8"))

    return executables


def processFile(file_path):
    final_dict = dict({})

    name = file_path.split('.exe')[0]
    final_dict[name] = getExecutables(file_path)

    return final_dict


def printFileExecutables(exe_dict):
    print("========================\n")
    print("Seções executáveis do PE\n")
    print("========================\n")
    for key in exe_dict:
        print(f'{key}: {exe_dict[key]}\n')


def processDir(file_path):
    final_dict = dict({})
    pe_files = os.listdir(file_path)

    for pe_file in pe_files:
        pe_file_path = str(file_path + "/" + pe_file)
        name = pe_file_path.split('.exe')[0]
        final_dict[name] = getExecutables(pe_file_path)

    return final_dict


def printDirExecutables(exe_dict):
    print("=========================\n")
    print("Seções executáveis por PE\n")
    print("=========================\n")
    for key in exe_dict:
        print(f'{key}: {exe_dict[key]}\n')


def main(argv):
    file_path = argv[0]

    if os.path.isdir(file_path):
        exe_dict = processDir(file_path)
        printDirExecutables(exe_dict)
    
    elif os.path.isfile(file_path):
        exe_dict = processFile(file_path)
        printFileExecutables(exe_dict)
    
    else:
        print("Por favor forneça um arquivo PE ou um diretório com arquivos PEs.")
    

if __name__ == "__main__":
    main(sys.argv[1:])