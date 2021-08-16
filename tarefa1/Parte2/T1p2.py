#!/usr/bin/python3

import sys

import pandas as pd
import re
import csv

def main(argv):
    """ The following input order must be respected:
        python3 T1p2.py sid-msg.map community.rules
    """
    # Protocols relations
    protocols = {
        "ip": 0,
        "tcp": 1,
        "udp": 2,
        "icmp": 3
    }

    # Variable used to build final data frame
    final_data = {
        "Protocolo": [],
        "Porta destino": [],
        "SID - Rotulo": []
    }

    # Reads first two columns of map into dict
    sid_map_df = pd.read_csv(argv[0], sep="\|\|", names=["Infos"], usecols=["Infos"], engine="python")
    community_rules = open(argv[1], "r")

    for line in community_rules:
        # Verifies if is a valid line
        valid = re.search("alert", line)
        if valid:
            parsed_line = line[valid.end() + 1:].split(" ")
            protocol = parsed_line[0]
            final_data["Protocolo"].append(protocols[protocol])

            # Destiny is the second word from the symbol "->" or "<>"
            try:
                sep_idx = parsed_line.index("->")
            except:
                sep_idx = parsed_line.index("<>")
            final_data["Porta destino"].append(parsed_line[sep_idx + 2])

            # Searchs for last sid occurrence position and parses string to get its number
            sid_idx = line.rfind("sid")
            sid_info = line[sid_idx:].split(";")[0]
            sid_number = int(sid_info.split(":")[1])
            final_data["SID - Rotulo"].append(sid_map_df.loc[sid_number]["Infos"].lstrip())

    community_rules.close()

    # Mounts and saves final csv file
    df = pd.DataFrame(final_data, columns=["Protocolo", "Porta destino", "SID - Rotulo"])
    df.to_csv(path_or_buf="T1p2.txt", index=False)

if __name__ == "__main__":
    main(sys.argv[1:])