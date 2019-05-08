#!/usr/bin/env python3
# vim: set syntax=python
"""Load data into the a pickle."""
import os
import argparse
import sys
import uuid
import logging

import pandas


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

NAMESPACE = uuid.UUID("7c375757-43f2-47e3-8e07-cab7d7726c37")


def create_hash(row):
    """Return a unique hash for a player based on their CSV row."""
    return str(
        uuid.uuid5(
            NAMESPACE,
            "{}{}{}".format(row["First Name"], row["Last Name"], row["DOB"])
        )
    )


def main(args):
    """Create new players, and create a new snapshot."""
    players = pandas.read_html(args.export_file, skiprows=0, header=0)[1]
    players["hash"] = players.apply(create_hash, axis=1)

    output_path = os.path.join(
        args.output_dir, os.path.splitext(args.export_file)[0])
    players.to_pickle(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "export_file",
        help=("HTML Report export from OOTP. Should have every column enabled "
              "and statistics from every level.")
    )
    parser.add_argument(
        "output_dir",
        help=("Directory to output the pickle to.")
    )
    args = parser.parse_args(sys.argv[1:])
    main(args)
