"""Packaging logic for python_parser."""

from __future__ import annotations

import os
import sys

import setuptools  # type: ignore[import]

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
setuptools.setup()
