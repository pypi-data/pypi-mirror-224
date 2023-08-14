from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from src.com_shining_brain.logger import setup_logger
import pandas as pd
import yaml
import re

logger = setup_logger("util.py")


def load_file_into_database(filename, table_name, column_mapping):
    Base = declarative_base()

    try:
        with open('db_config.yaml', 'r') as file:
            db_config = yaml.safe_load(file)

        url = f'mysql+mysqlconnector://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}/{db_config["database"]}'
        engine = create_engine(url)
        Base.metadata.create_all(engine)

        if filename.endswith('.csv'):
            df = pd.read_csv(filename)
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(filename)
        else:
            logger.warning('Unknown file type')
            return

        df.rename(columns=column_mapping, inplace=True)
        df.to_sql(table_name, con=engine, index=False, if_exists='replace')
        logger.info('Data successfully loaded into the database')

    except Exception as e:
        logger.error(f'An error occurred while loading the file into the database: {e}')


def map_dtype(dtype):
    if "int" in str(dtype):
        return "int"
    elif "float" in str(dtype):
        return "decimal(16,6)"
    elif "datetime" in str(dtype):
        return "datetime"
    else:
        return "varchar(50)"


def to_snake_case(s):
    s = s.replace(' ', '')
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    s = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s)
    return re.sub(r'\W+', '_', s).lower()


def generate_ddl_from_csv(excel_path, table_name="table_name"):
    df = pd.read_csv(excel_path, nrows=2)

    ddl = f"create table {table_name} (\n"
    ddl += "    id bigint auto_increment primary key,\n"
    for column, dtype in df.dtypes.items():
        mysql_type = map_dtype(dtype)
        ddl += f"    {to_snake_case(column)} {mysql_type},\n"

    ddl += "    created datetime default current_timestamp () not null,\n"
    ddl += "    updated datetime default current_timestamp () not null,\n"
    return ddl.rstrip(",\n") + "\n);"
