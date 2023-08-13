"""Loads Python file content into string, and performs checks on Python
files."""
import filecmp
import json
import os
import subprocess  # nosec
from typing import Any, Dict, List

from src.python_parser.PythonStructures import Docstring


def write_dict_to_json(data: Dict[str, Any], filepath: str) -> None:
    """Write a dictionary to a JSON file.

    Args:
        data (Dict[str, Any]): The dictionary to be written.
        filename (str): The name of the JSON file to create or overwrite.
    """
    with open(filepath, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


def load_dict_from_json(filename: str) -> Dict[str, Any]:
    """Load a dictionary from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        Dict[str, Any]: The dictionary loaded from the JSON file.
    """
    with open(filename, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def format_python_file(file_path: str) -> None:
    """Format a Python file using the Black code formatter.

    Args:
        file_path (str): Path to the Python file.
    """
    subprocess.run(["black", file_path], check=True)  # nosec


def files_have_identical_content(file1: str, file2: str) -> bool:
    """Check if two files have identical content.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.

    Returns:
        bool: True if the files have identical content, False otherwise.
    """
    return filecmp.cmp(file1, file2, shallow=False)


def get_file_content(file_path: str) -> str:
    """Get the content of the specified file.

    Args:
        file_path (str): Path to the Python file.

    Returns:
        str: Content of the file if found. Raises error otherwise.
    """
    if os.path.exists(file_path):
        with open(file_path, encoding="utf-8") as file:
            content = file.read()
        return content
    raise FileNotFoundError(f"File '{file_path}' not found.")


def set_file_content(file_path: str, content: str) -> None:
    """Set the content of the specified file.

    Args:
        file_path (str): Path to the Python file.
        content (str): Content to write into the file.
    """

    if os.path.exists(file_path):
        raise FileExistsError(f"File '{file_path}' already exists.")

    with open(file_path, "w", encoding="utf-8") as file:
        # file.write(content)
        file.write(content)


def delete_file_if_exists(file_path: str) -> None:
    """Delete a file if it exists.

    :param file_path: The path to the file to be deleted.
    :type file_path: str
    """
    if os.path.exists(file_path):
        os.remove(file_path)


def get_initial_docstring_from_file(file_path: str) -> Docstring:
    """Extract the initial docstring from a Python file.

    Args:
        file_path (str): Path to the Python file.

    Returns:
        str: Initial docstring content.
    """
    with open(file_path, encoding="utf-8") as file:
        lines = file.readlines()

    return get_initial_docstring_from_content(lines)


def get_initial_docstring_from_content(lines: List[str]) -> Docstring:
    """Extract the initial docstring from a Python file content.

    Args:
        lines (List[str]): List with lines of Python file as strings.

    Returns:
        str: Initial docstring content.
    """
    docstring = ""
    in_docstring = False
    for line in lines:
        stripped_line = line.strip()

        if stripped_line.startswith('"""') or stripped_line.startswith("'''"):
            if in_docstring:
                docstring += line
                break  # Exiting the docstring
            in_docstring = True
            docstring += line
        elif in_docstring:
            docstring += line
        elif stripped_line and not stripped_line.startswith("#"):
            break  # Exiting the docstring block

    return Docstring(docstring=docstring.strip())
