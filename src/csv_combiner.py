from io import StringIO
from typing import List
import pandas as pd
import os


class CSVCombiner:
    """
    Description: Numpy Style
    """

    def __init__ (self, csv_list:List)-> None:
            self.csv_list = csv_list

    def combine(self, add_csv_name = True) -> pd.DataFrame:
        df_list = []

        for csv_file in self.csv_list:
            df_temp = pd.read_csv(csv_file)
            if add_csv_name:
                file_name = csv_file.split('/')[-1]
                df_temp['filename'] = file_name
            df_list.append(df_temp)

        return pd.concat(df_list)
    
    def get_csv(self) -> None:
        output = StringIO()
        self.combine().to_csv(output, index = False)
        print(output.getvalue())