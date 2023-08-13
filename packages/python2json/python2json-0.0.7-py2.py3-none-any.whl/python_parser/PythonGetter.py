"""Convert Python file content to modular Python code storage structures, and
from those code structures to Json."""
import ast
import json
from typing import List, Union

import astunparse

from src.python_parser.file_parsing import (
    delete_file_if_exists,
    files_have_identical_content,
    format_python_file,
    set_file_content,
    write_dict_to_json,
)
from src.python_parser.HC import HC
from src.python_parser.PythonSetter import PythonSetter
from src.python_parser.PythonStructures import (
    ArgStorage,
    ClassStorage,
    CodeStorage,
    Docstring,
    DocumentationStorage,
    JsonContent,
    MethodsStorage,
)


# pylint: disable=R0902
class PythonGetter:
    """A class to convert Python file content to modular Python code storage
    structures, and from those code structures to Json."""

    def __init__(self, python_content: str, file_dir: str, raw_filename: str):
        self.python_content: str = python_content
        self.file_dir: str = file_dir
        self.raw_filename: str = raw_filename
        self.tree: ast.Module = ast.parse(self.python_content)
        self.json_content: JsonContent = self.code_to_structure(tree=self.tree)

        # Write python code to dummy file.
        self.hardcoded: HC = HC()
        self.original_py_filepath: str = f"{file_dir}{raw_filename}.py"
        # TODO: assert file does not yet exist.
        self.dummy_filepath: str = (
            f"{file_dir}{self.hardcoded.reconstruct_id}{raw_filename}.py"
        )
        self.json_dummy_filepath: str = (
            f"{file_dir}{self.hardcoded.reconstruct_id}{raw_filename}.json"
        )

        write_dict_to_json(
            data=self.json_content.to_dict(), filepath=self.json_dummy_filepath
        )

        self.verify_code_retrievability(
            dummy_filepath=self.dummy_filepath,
            original_py_filepath=self.original_py_filepath,
            json_content=self.json_content,
            file_dir=self.file_dir,
            raw_filename=self.raw_filename,
        )

    def code_to_structure(self, tree: ast.Module) -> JsonContent:
        """Extracts class names and docstrings from Python content.

        Returns:
            List[Dict[str, str]]: List of dictionaries containing class names
            and docstrings.
        """
        # print(python_content)  # Used to get file docstring.
        json_content: JsonContent = ast_to_json_content(tree=tree)
        return json_content

    def convert_structure_to_json(self, json_content: JsonContent) -> str:
        """Converts Python code structures to modular JSON.

        Returns:
            str: JSON string representing modular structure.
        """
        raw_content: str = json.dumps(json_content.to_dict(), indent=4)
        return raw_content

    # pylint: disable=R0913
    def verify_code_retrievability(
        self,
        dummy_filepath: str,
        original_py_filepath: str,
        json_content: JsonContent,
        file_dir: str,
        raw_filename: str,
    ) -> None:
        """Verifies that the json file can be convert back into the original
        Python file before proceeding."""
        python_setter: PythonSetter = PythonSetter(
            file_dir=file_dir, raw_filename=raw_filename
        )

        # Convert JSON filecontent back to JsonContent object.
        json_content: JsonContent = (
            python_setter.convert_from_json_to_structure(
                json_dict=json_content.to_dict()
            )
        )
        # Convert the JsonContent structure back to Python code.
        python_code: str = python_setter.structure_to_python(
            json_content=json_content
        )

        delete_file_if_exists(file_path=dummy_filepath)
        set_file_content(file_path=dummy_filepath, content=python_code)

        # Apply black formatting to original Python file and dummy file.
        format_python_file(file_path=original_py_filepath)
        format_python_file(file_path=dummy_filepath)

        # Verify python file contents are identical.
        if not files_have_identical_content(
            file1=original_py_filepath, file2=dummy_filepath
        ):
            print("Original:")
            print(original_py_filepath)
            print("Reconstructed:")
            print(dummy_filepath)
            raise ValueError(
                "Error, the reconstructed python file is not identical to the "
                + "original Python file."
            )


def convert_arg(node: ast.arg) -> ArgStorage:
    """Converts a class into a Python storage structure for a class or method
    argument."""
    if node.annotation is None:
        return ArgStorage(name=node.arg)
    return ArgStorage(argType=node.annotation.id, name=node.arg)


def convert_function(
    node: ast.FunctionDef, hc: HC, indentation: int
) -> MethodsStorage:
    """Converts a class into a Python storage structure for a method."""
    arguments = [convert_arg(arg) for arg in node.args.args]
    children: List[Union[ClassStorage, MethodsStorage, CodeStorage]] = []
    for stmt in node.body:
        if isinstance(stmt, ast.FunctionDef):
            children.append(
                convert_function(
                    node=stmt,
                    hc=hc,
                    indentation=indentation + hc.indent_spaces,
                )
            )
        elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Str):
            children.append(
                DocumentationStorage(
                    documentation_content=stmt.value.s, indentation=indentation
                )
            )
        else:
            source_code: str = astunparse.unparse(stmt)
            print("STARTsource_code")
            print(source_code)
            print("ENDsource_code")
            children.append(
                CodeStorage(
                    code_content=source_code,
                    indentation=indentation,
                )
            )

    if node.returns is None:
        returnType = ""
    else:
        if "id" in node.returns.__dict__.keys():
            returnType = node.returns.id
        else:
            returnType = node.returns.value

    return MethodsStorage(
        arguments=arguments,
        children=children,
        documentation=ast.get_docstring(node) or "",
        name=node.name,
        returnType=returnType,
    )


def convert_class(
    node: ast.ClassDef, hc: HC, indentation: int
) -> ClassStorage:
    """Converts a class into a Python storage structure for a class."""
    arguments = [
        convert_arg(arg) for arg in node.body if isinstance(arg, ast.arg)
    ]
    children = []
    for stmt in node.body:
        if isinstance(stmt, ast.FunctionDef):
            children.append(
                convert_function(
                    node=stmt,
                    hc=hc,
                    indentation=indentation + hc.indent_spaces,
                )
            )
        elif isinstance(stmt, ast.ClassDef):
            children.append(
                convert_class(
                    node=stmt,
                    hc=hc,
                    indentation=indentation + hc.indent_spaces,
                )
            )
        elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Str):
            children.append(
                CodeStorage(
                    code_content=stmt.value.s,
                    indentation=indentation + hc.indent_spaces,
                )
            )
    return ClassStorage(
        documentation=ast.get_docstring(node) or "",
        name=node.name,
        arguments=arguments,
        children=children,
        returnType=None,  # Class definitions don't have a return type
    )


def ast_to_json_content(tree: ast.Module) -> JsonContent:
    """Converts an abstract syntax tree to a Python storage structure."""
    code_elems = []
    docstring = ""
    hc: HC = HC()

    for node in tree.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
            docstring = node.value.s
        elif isinstance(node, ast.FunctionDef):
            code_elems.append(
                convert_function(
                    node=node, hc=hc, indentation=0 + hc.indent_spaces
                )
            )
        elif isinstance(node, ast.ClassDef):
            code_elems.append(
                convert_class(
                    node=node, hc=hc, indentation=0 + hc.indent_spaces
                )
            )

    return JsonContent(
        docstring=Docstring(docstring=docstring), code_elems=code_elems
    )
