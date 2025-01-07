import os
from etl.extract import extract_repo
from etl.transform import transform_data
from etl.load import load_data

def main():
    # Fetch dynamic values from environment variables
    repo_url = os.getenv("REPO_URL")  # Repository URL
    local_path = os.getenv("LOCAL_PATH", "repo")  # Default local path
    db_url = os.getenv("DB_URL", "sqlite:///etl_data.db")  # Default database URL
    table_name = os.getenv("TABLE_NAME", "etl_table")  # Default table name

    if not repo_url:
        raise ValueError("REPO_URL environment variable is required")

    # ETL Pipeline
    extract_repo(repo_url, local_path)
    file_paths = [f"{local_path}/example_file.txt"]  # Add logic to list actual files
    df = transform_data(file_paths)
    load_data(df, db_url, table_name)

if __name__ == "__main__":
    main()
