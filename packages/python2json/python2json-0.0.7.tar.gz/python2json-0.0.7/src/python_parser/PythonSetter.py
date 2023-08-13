"""Convert a JSON filecontent back into modular Python code storage structures,
and from those code structures back to a Python filecontent."""

from typing import Any, Dict, List, Union

from src.python_parser.file_parsing import load_dict_from_json
from src.python_parser.HC import HC
from src.python_parser.PythonStructures import (
    ArgStorage,
    ClassStorage,
    CodeStorage,
    DocumentationStorage,
    JsonContent,
    MethodsStorage,
)


class PythonSetter:
    """A class to convert a JSON filecontent back into modular Python code
    storage structures, and from those code structures back to a Python
    filecontent."""

    def __init__(self, file_dir: str, raw_filename: str):
        self.file_dir: str = file_dir
        self.raw_filename: str = raw_filename

        # Write python code to dummy file.
        self.hardcoded: HC = HC()
        self.json_dummy_filepath: str = (
            f"{file_dir}{self.hardcoded.reconstruct_id}{raw_filename}.json"
        )

        self.json_dict: Dict[str, Any] = load_dict_from_json(
            filename=self.json_dummy_filepath
        )
        self.json_content: JsonContent = self.convert_from_json_to_structure(
            json_dict=self.json_dict
        )
        self.python_code: str = self.structure_to_python(
            json_content=self.json_content
        )

    def convert_from_json_to_structure(
        self, json_dict: Dict[str, Any]
    ) -> JsonContent:
        """Converts modular JSON back to Python code structures.

        Args:
            json_content (str): JSON content.

        Returns:
            str: Python file content.
        """
        json_content: JsonContent = JsonContent(
            docstring=json_dict["docstring"],
            code_elems=self.children_to_python_structure(
                json_list=json_dict["code_elems"]
            ),
        )
        return json_content

    def children_to_python_structure(
        self, json_list: List[Dict]
    ) -> List[Union[ClassStorage, MethodsStorage, CodeStorage]]:
        """Recursively convert a list of child elements into Python structure
        objects."""
        children: List[Union[ClassStorage, MethodsStorage, CodeStorage]] = []
        child: Dict
        for child in json_list:
            if "class" in child:
                children.append(self.json_str_to_class(child=child))
            elif "method" in child:
                children.append(self.json_str_to_method(child=child))
            elif "code_content" in child:
                children.append(CodeStorage(**child))
            elif "documentation_content" in child:
                children.append(DocumentationStorage(**child))
            else:
                raise KeyError(f"Error did not expect key:{child}")
        return children

    def json_str_to_class(self, child: Dict) -> ClassStorage:
        """Converts a child dictionary back into a ClassStorage object."""
        class_storage = ClassStorage(
            documentation=child["class"]["documentation"],
            name=child["class"]["name"],
            arguments=list(
                map(
                    lambda arg: ArgStorage(
                        argType=arg["argtype"],
                        name=arg["name"],
                    ),
                    child["class"]["arguments"],
                )
            ),
            children=self.children_to_python_structure(
                child["class"]["children"]
            ),
            returnType=child["class"]["returnType"],
        )
        return class_storage

    def json_str_to_method(self, child: Dict) -> MethodsStorage:
        """Converts a child dictionary back into a MethodsStorage object."""
        argList: List[ArgStorage] = list(
            map(
                lambda arg: ArgStorage(**arg),
                child["method"]["arguments"],
            )
        )
        method_storage = MethodsStorage(
            documentation=child["method"]["documentation"],
            name=child["method"]["name"],
            arguments=argList,
            children=self.children_to_python_structure(
                child["method"]["children"]
            ),
            returnType=child["method"]["returnType"],
        )
        return method_storage

    def structure_to_python(self, json_content: JsonContent) -> str:
        """Converts Python code structure back to Python file content.

        Args:
            json_content (str): JSON content.

        Returns:
            Optional[str]: Python file content, or None if conversion fails.
        """
        return json_content.to_python_string()
