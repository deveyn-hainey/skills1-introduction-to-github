import pandas as pd
from etl.load import load_data
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

def test_load_data():
    df = pd.DataFrame({'file_path': ['test_file'], 'line_count': [3]})
    db_url = "sqlite:///:memory:"
    table_name = "test_table"
    
    # Test data loading
    try:
        load_data(df, db_url, table_name)
        engine = create_engine(db_url)
        loaded_df = pd.read_sql_table(table_name, engine)
        assert loaded_df.equals(df)
    except OperationalError:
        assert False, "Data loading failed"

