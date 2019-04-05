#!/usr/bin/env python3
# vim: set syntax=python
"""Load data into the DB."""
import argparse
import sys
import uuid
from datetime import datetime
import logging

import pandas

from base import db
from db.constants import (
    INFO_FIELDS,
    RATINGS_FIELDS,
)
from db.models import (
    Player,
    Snapshot,
    Ratings,
)


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

NAMESPACE = uuid.UUID("7c375757-43f2-47e3-8e07-cab7d7726c37")


def create_hash(row):
    return str(
        uuid.uuid5(
            NAMESPACE,
            "{}{}{}".format(row["First Name"], row["Last Name"], row["DOB"])
        )
    )


def main(args):
    logger.info("Getting existing players.")
    existing_players = Player.query.all()
    existing_hashes = [
        player.hash
        for player in existing_players
    ]
    logger.info("Loaded {} players.".format(len(existing_hashes)))

    players = pandas.read_html(args.export_file, skiprows=0, header=0)[1]

    players["hash"] = players.apply(create_hash, axis=1)

    # insert players
    new_players = [
        Player(
            hash=row["hash"],
            first_name=row["First Name"],
            last_name=row["Last Name"],
            date_of_birth=datetime.strptime(row["DOB"], "%m/%d/%Y"),
        )
        for _, row in players.iterrows()
        if row["hash"] not in existing_hashes
    ]
    logger.info("Adding {} new players.".format(len(new_players)))

    db.session.add_all(new_players)

    logger.info("Creating snapshot for {}".format(args.snapshot_date))
    snapshot = Snapshot(date=datetime.strptime(args.snapshot_date, "%Y-%m-%d"))
    db.session.add(snapshot)

    logger.info("Loading snapshot data.")
    all_players = Player.query.all()
    hash_to_player = {
        player.hash: player
        for player in all_players
    }

    ratings = [
        Ratings(
            snap_shot=snapshot,
            player=hash_to_player[row["hash"]],
            **{
                db_field: row[ootp_field]
                for ootp_field, db_field in INFO_FIELDS.items()
            },
            **{
                db_field: row[ootp_field]
                for  ootp_field, db_field in RATINGS_FIELDS.items()
            },
        )
        for _, row in players.iterrows()
    ]
    db.session.add_all(ratings)

    db.session.commit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "export_file",
        help=("HTML Report export from OOTP. Should have every column enabled "
              "and statistics from every level.")
    )
    parser.add_argument(
        "snapshot_date",
        help=("Date of the export, in YYYY-MM-DD format.")
    )
    args = parser.parse_args(sys.argv[1:])
    main(args)
