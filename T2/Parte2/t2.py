#!/usr/bin/python3

import sys
import pefile

# Reference: https://docs.microsoft.com/en-us/windows/win32/debug/pe-format?redirectedfrom=MSDN#section-table-section-headers
READEBLE_SECTION = 0x40000000
WRITEBLA_SECTION = 0x80000000
EXECUTABLE_SECTION = 0x20000000

def sectionAnalisys(section):
    options = {
        "read": "-",
        "write": "-",
        "execute": "-"
    }

    characteristics = getattr(section, 'Characteristics')
    if characteristics & READEBLE_SECTION > 0:
        options["read"] = "r"
    
    if characteristics & WRITEBLA_SECTION > 0:
        options["write"] = "w"
    
    if characteristics & EXECUTABLE_SECTION > 0:
        options["execute"] = "x"

    return options


def main(argv):
    """ The following input order must be respected:
        python3 
    """
    pe_first = pefile.PE(argv[0])
    pe_second = pefile.PE(argv[1])

    pe_first_sections = set({})
    pe_first_options = dict({})
    for section in pe_first.sections:
        name = str(section.Name.decode("utf-8"))
        pe_first_sections.add(name)
        pe_first_options[name] = sectionAnalisys(section)

    pe_second_sections = set({})
    pe_second_options = dict({})
    for section in pe_second.sections:
        name = str(section.Name.decode("utf-8"))
        pe_second_sections.add(name)
        pe_second_options[name] = sectionAnalisys(section)

    intersection = pe_first_sections.intersection(pe_second_sections)
    pe_first_only = pe_first_sections.difference(pe_second_sections)
    pe_second_only = pe_second_sections.difference(pe_first_sections)

    print(f'Binários {argv[0]} e {argv[1]} contém as seguintes seções em comum:')
    for item in intersection:
        options = pe_first_options[item]
        if options["execute"] == "x":
            print(f'Seção: {item} é executável: {options["read"]}{options["write"]}{options["execute"]}')
        else:
            print(f'Seção: {item} não é executável: {options["read"]}{options["write"]}{options["execute"]}')

    print(f'Apenas binário {argv[0]} contém as seguintes seções:')
    for item in pe_first_only:
        options = pe_first_options[item]
        if options["execute"] == "x":
            print(f'Seção: {item} é executável: {options["read"]}{options["write"]}{options["execute"]}')
        else:
            print(f'Seção: {item} não é executável: {options["read"]}{options["write"]}{options["execute"]}')

    print(f'Apenas binário {argv[1]} contém as seguintes seções:')
    for item in pe_second_only:
        options = pe_second_options[item]
        if options["execute"] == "x":
            print(f'Seção: {item} é executável: {options["read"]}{options["write"]}{options["execute"]}')
        else:
            print(f'Seção: {item} não é executável: {options["read"]}{options["write"]}{options["execute"]}')
    

if __name__ == "__main__":
    main(sys.argv[1:])