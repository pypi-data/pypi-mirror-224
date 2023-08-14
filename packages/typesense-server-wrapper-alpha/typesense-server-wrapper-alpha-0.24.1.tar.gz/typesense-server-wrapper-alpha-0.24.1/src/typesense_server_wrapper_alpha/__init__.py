"""Typesense Server Wrapper Alpha"""

import pathlib


def get_path():
    file_path = pathlib.Path(__file__)
    bin_path = (file_path.parent / 'typesense-server.1.bin').resolve()
    return bin_path


__title__ = 'typesense-server-wrapper-alpha'
__version__ = '0.24.1'
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = '2023, Grant Jenks'
