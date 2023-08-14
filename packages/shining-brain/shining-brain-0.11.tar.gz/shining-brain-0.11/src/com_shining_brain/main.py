from util import load_file_into_database
from logger import setup_logger

logger = setup_logger('main.py')


if __name__ == '__main__':
    filename = "/Users/thomas/Documents/english-language/wordbank.csv"
    column_mapping = {
        'Word': 'word',
        'Search Date': 'search_date',
        'Class': 'class'
    }
    table_name = 'test_wordbank'
    load_file_into_database(filename, table_name, column_mapping)
