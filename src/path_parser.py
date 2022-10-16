import sys
import os
from typing import List

class PathParser:
    def __init__(self, path_list:List = sys.argv) -> None:
        self.path_list = path_list

    def get_paths(self) -> List:
        return self.path_list[1:]