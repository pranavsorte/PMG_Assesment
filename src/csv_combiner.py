from io import StringIO
from typing import List
import pandas as pd


class CSVCombiner:
    """
    This class combines all CSVs from the given list of the paths. 

    Methods:
    --------
    __init__:
        Class constructor.

    combine:
        Combines CSVs and adds extra column of `filename`.

    get_csv:
        Throws output to `stdout`
    
    Examples:
    ---------
    >>> path_list = ['./csv/clothing.csv', './csv/accessories.csv']
    >>> combiner = CSVCombiner(path_list)
    >>> combiner.get_csv()
    email_hash,category,filename
    b9f6f22276c919da793da65c76345ebb0b072257d12402107d09c89bc369a6b6,Satchels,accessories.csv
    """

    def __init__ (self, csv_list:List)-> None:
        """
        Constructor of the class

        Parameters:
        -----------

        csv_list:List
            List of strings. These strings are supposebly paths.
        """
        self.csv_list = csv_list

    def combine(self, add_csv_name:bool = True) -> pd.DataFrame:
        """
        This method combines all CSVs and adds extra column to final CSV. This extra column is filename of originally concatenated files. 

        Parameters:
        -----------
        
        add_csv_name:bool 
            If this parameter is `True`, new column will be added as described above. 

        Returns:
        --------
        pd.Dataframe:
            A single pandas Dataframe with all CSVs concatenated.

        """
        df_list = []

        for csv_file in self.csv_list:
            try:
                df_temp = pd.read_csv(csv_file)
            except:
                raise Exception('File not present or incorrect path')

            if add_csv_name:
                file_name = csv_file.split('/')[-1]
                df_temp['filename'] = file_name

            df_list.append(df_temp)

        same_columns = all([len(df_list[0].columns.intersection(df.columns)) == df_list[0].shape[1] for df in df_list])

        if not same_columns:
            raise Exception('CSVs do not have same columns')    

        try:
            return pd.concat(df_list)
        except:
            raise Exception('Error while combining CSVs. Please check files and/or paths')
    
    def get_csv(self) -> None:
        """
        Throws output of Pandas dataframe to `stdout`
        """
        output = StringIO()
        self.combine().to_csv(output, index = False)
        print(output.getvalue())