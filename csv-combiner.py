from src.csv_combiner import CSVCombiner
from src.path_parser import PathParser


def main():
    all_paths = PathParser()
    csv_c = CSVCombiner(all_paths.get_paths())


    return csv_c.get_csv()

if __name__ == "__main__":
    main()