from sqlalchemy import create_engine

def load_data(df, db_url, table_name):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Data loaded into {table_name}")
