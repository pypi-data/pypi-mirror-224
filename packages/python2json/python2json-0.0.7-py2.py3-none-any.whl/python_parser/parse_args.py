"""Parses CLI arguments for the API interactions."""
import argparse


def parse_api_args() -> argparse.Namespace:
    """Reads command line arguments and converts them into Python arguments."""
    parser = argparse.ArgumentParser(
        description="Convert Python file to JSON and back."
    )

    parser.add_argument(
        "action",
        choices=["get_json", "set_json"],
        help="get: convert Python file to JSON file, or set: JSON filecontent "
        + "as Python file.",
    )
    parser.add_argument("file_path", help="Path to the Python file")

    args = parser.parse_args()
    return args
