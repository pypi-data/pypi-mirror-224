"""Processes API arguments and performs the requested actions."""
from argparse import Namespace

from src.python_parser.file_parsing import get_file_content, set_file_content


def process_api_args(args: Namespace) -> None:
    """Processes the arguments and performs the requested actions."""
    if args.action == "get":
        content = get_file_content(args.file_path)
        if content is not None:
            print(content)

        # TODO: Apply Black formatting.
        # TODO: Convert Python filecontent to Json filecontent.
        # TODO: Write JSON filecontent to file.
        # TODO: Verify JSON filecontent can be reversed to original .py file.
    elif args.action == "set":
        content = input("Enter content to write to the file:\n")

        # TODO: Convert JSON filecontent to Python filecontent.
        # TODO: Write Python filecontent to file.
        set_file_content(args.file_path, content)
