#!/usr/bin/python3

import sys
import os

import pefile


def getSections(file_path):
    pe_sections = set([])
    pe = pefile.PE(file_path)
    
    for section in pe.sections:
        pe_sections.add(section.Name.decode("utf-8"))

    return pe_sections


def printUniqueSections(path_fst, path_scd, pe_fst_sections, pe_scd_sections):
    pe_fst_only = pe_fst_sections.difference(pe_scd_sections)
    pe_scd_only = pe_scd_sections.difference(pe_fst_sections)

    print("========================\n")
    print("Permissões únicas por PE\n")
    print("========================\n")
    print(f'{path_fst}: {list(pe_fst_only)}')
    print(f'{path_scd}: {list(pe_scd_only)}')


def printSharedSections(path_fst, path_scd, pe_fst_sections, pe_scd_sections):
    intersection = pe_fst_sections.intersection(pe_scd_sections)

    print("=========================\n")
    print("Permissões comuns dos PEs\n")
    print("=========================\n")
    print(list(intersection))

def main(argv):
    path_fst = argv[0]
    path_scd = argv[1]
    if (not os.path.isfile(path_fst)) or (not os.path.isfile(path_scd)):
        print("Por favor forneça dois arquivos PE")
        sys.exit(0)

    pe_fst_sections = getSections(path_fst)
    pe_scd_sections = getSections(path_scd)

    printUniqueSections(path_fst, path_scd, pe_fst_sections, pe_scd_sections)
    printSharedSections(path_fst, path_scd, pe_fst_sections, pe_scd_sections)

if __name__ == "__main__":
    main(sys.argv[1:])