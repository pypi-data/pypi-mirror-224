"""Entry point for the project."""

from src.python_parser.parse_args import parse_api_args
from src.python_parser.process_args import process_api_args

api_args = parse_api_args()
process_api_args(api_args)
