import sys
from typing import List

class PathParser:
    """
    This class generate list of paths from `stdin`

    Methods:
    --------
    
    __init__:
        Class Constructor.
    
    get_paths:
    ----------
        Generates list of path:strings.
    """
    def __init__(self, path_list:List = sys.argv) -> None:
        """
        Class constructor.

        Parameters:
        -----------
        path_list:List
            Default: `sys.argv`
            List of inputs
        """
        self.path_list = path_list

    def get_paths(self) -> List:
        """
        This method generates all paths.

        Returns:
        --------
        List of paths
        """
        
        return self.path_list[1:]