import unittest
from src.csv_combiner import CSVCombiner
from src.path_parser import PathParser

class TestCSVCombiner(unittest.TestCase):
    """
    This class is designed for running unit tests on the csv_combiner and path_parses classes. 

    Methods:
    --------
    test_check_output:
        Used test to check output of files.

    test_check_path:
        Unit test to check if the path of file is valid.
    
    test_check_csv:
        Unit test to check the csv file.
    
    test_different_columns:
        Unit test to check if the columns match
        
    """
    
    def test_check_output(self):
        """
        This unit test method is to check the output of the concantenated file. If all the parameters 
        which are passed to csv_combiner and path_parser are valid, the test runs without any raised exception

        """
        self.path = ['./fixtures/clothing.csv']
        csv_c = CSVCombiner(self.path)
        self.assertEqual(csv_c.get_csv(), None)
    
    def test_check_path(self):
        """
        This unit test method is to check the path of the file. 
        The method catches the raised exception generated after passing invalid path

        """
        self.path = ['asd']
        csv_c = CSVCombiner(self.path)
        with self.assertRaises(Exception) as context:
            csv_c.get_csv()
        self.assertEqual('File not present or incorrect path', str(context.exception))


    def test_check_csv(self):
        """
        This unit test method is to check the output generated after combining CSV files.
        The method catches the raised exception generated after invalid parameters to csv_combiner

        """
        self.path = []
        csv_c = CSVCombiner(self.path)
        with self.assertRaises(Exception) as context:
            csv_c.get_csv()
        self.assertEqual('Error while combining CSVs. Please check files and/or paths', str(context.exception))

    def test_different_columns(self):
        """
        This unit test method is to check the columns of the files to be combined
        The method catches the raised exception when files of different columns are passed

        """
        self.path = ['./fixtures/clothing.csv','./clothing_different_columns.csv']
        csv_c = CSVCombiner(self.path)
        with self.assertRaises(Exception) as context:
            csv_c.get_csv()
        self.assertEqual('CSVs do not have same columns', str(context.exception))
               

if __name__ == "__main__":
    unittest.main()
