import argparse

version = "v1"

def get_args():
    parser = argparse.ArgumentParser(description=f"ntcleaner {version}")

    parser.add_argument(
        "-chrome",
        action="store_true",
        help="clear Google Chrome cache"
    )

    parser.add_argument(
        "-firefox",
        action="store_true",
        help="clear Firefox cache"
    )

    parser.add_argument(
        "-wupdate",
        action="store_true",
        help="clear Windows Update cache"
    )
    
    return parser.parse_args()
