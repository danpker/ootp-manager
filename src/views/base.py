"""Common functions and variables for all views."""
import os

DATA_DIR = os.environ.get("DATA_DIR")
SNAPSHOTS = os.listdir(DATA_DIR)
LATEST_SNAPSHOT = max(SNAPSHOTS)


def snapshot_to_path(snapshot):
    """Return the snapshot's path."""
    return os.path.join(DATA_DIR, snapshot)
