#!/usr/bin/python3

import sys

import pandas as pd


def main(argv):
    """ The following input order must be respected:
        python3 T1p1b.py AV2.txt
    """
    # Reads input, first column only
    df = pd.read_csv(argv[0], sep=":", names=["Sys info"], usecols=["Sys info"])

    # Removes unwanted string from column
    df["Sys info"] = df["Sys info"].str.replace("PUA.", '')

    # Splits as necessary and drops unnecessary columns
    df[["Plataforma/Linguagem", "Tipo", "Subtipo"]] = df["Sys info"].str.split('.', 2, expand=True)
    df = df.drop(columns=["Sys info"])
    df[["Subtipo", "Variante"]] = df["Subtipo"].str.split('-', 1, expand=True)

    # Saves final csv file
    df.to_csv(path_or_buf="T1p1b.txt", index=False)

if __name__ == "__main__":
    main(sys.argv[1:])