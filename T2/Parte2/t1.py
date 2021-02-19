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
    pe = pefile.PE(argv[0])

    for section in pe.sections:
        options = sectionAnalisys(section)
        if options["execute"] == "x":
            print(f'Seção: {section.Name.decode("utf-8")} é executável: {options["read"]}{options["write"]}{options["execute"]}')
        else:
            print(f'Seção: {section.Name.decode("utf-8")} não é executável: {options["read"]}{options["write"]}{options["execute"]}')
    

if __name__ == "__main__":
    main(sys.argv[1:])