#!/usr/bin/python3

import sys

import pandas as pd


def main(argv):
    """ The following input order must be respected:
        python3 T1p1a.py AV1.txt
    """
    # Reads all columns of input into dataframe
    df = pd.read_csv(argv[0], sep=":", names=["Info 1", "Info 2", "Virus info"])

    # Splits necessary column and drops unnecessary
    df[["SO","Virus"]] = df["Virus info"].str.split('.', 1, expand=True)
    df = df.drop(columns=["Info 1", "Info 2", "Virus info"])

    # Drops duplicates to calculate variants only
    df = df.drop_duplicates(["Virus"])

    # Split again in order to format "Virus" as wanted and drops unnecessary
    df[["Virus", "Variant"]] = df["Virus"].str.split('-', 1, expand=True)
    df = df.drop(columns=["SO"]).dropna()

    # Group by virus and count variants
    df = df.groupby(["Virus"]).count()

    # Saves final csv file
    df.to_csv(path_or_buf="T1p1a.txt", header=False)

if __name__ == "__main__":
    main(sys.argv[1:])