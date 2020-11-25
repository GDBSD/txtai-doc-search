import os
from os.path import dirname

"""
Simple helper utility to make dealing with file paths easier.
"""

PROJECT_PATH = dirname(os.path.abspath(__file__))
SRC_PATH = f'{PROJECT_PATH}/src'
APP_PATH = f'{SRC_PATH}/docsearch'
DATA_PATH = f'{PROJECT_PATH}/data'


def create_paths_helper():
    return PathsHelper()


class PathsHelper:
    def __init__(self):
        self.paths = {
            'src': SRC_PATH,
            'data': DATA_PATH,
            'app': f'{SRC_PATH}/docsearch',
            'test_data': f'{PROJECT_PATH}/tests/test_data'
        }

    def path_src(self, subdirectory=''):
        return '{}/{}'.format(self.paths['src'], subdirectory)

    def path_data(self):
        return self.paths['data']

    def path_app(self):
        return self.paths['app']

    def path_test_data(self):
        return self.paths['test_data']

