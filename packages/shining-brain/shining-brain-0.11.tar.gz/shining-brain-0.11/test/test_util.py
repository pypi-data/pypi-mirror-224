from src.my_package.util import generate_ddl_from_csv
import pandas as pd


def test_generate_ddl_from_csv():
    df = pd.DataFrame({
        'Name': ['Alice'],
        'Start Date': ['2020-02-02'],
        'Age': [18],
        'Salary': [5000.50],
    })
    df.to_csv('./data_for_test_generate_ddl_from_csv.csv', index=False)

    expected_ddl = (
        "create table table_001 (\n"
        "    id bigint auto_increment primary key,\n"
        "    name varchar(50),\n"
        "    start_date varchar(50),\n"
        "    age int,\n"
        "    salary decimal(16,6),\n"
        "    created datetime default current_timestamp () not null,\n"
        "    updated datetime default current_timestamp () not null\n"
        ");"
    )

    assert generate_ddl_from_csv('./data_for_test_generate_ddl_from_csv.csv', 'table_001') == expected_ddl
