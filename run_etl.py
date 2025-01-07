from etl.extract import extract_repo
from etl.transform import transform_data
from etl.load import load_data

def main():
    repo_url = "https://github.com/example/example-repo.git"
    local_path = "repo"
    db_url = "sqlite:///etl_data.db"
    table_name = "etl_table"

    # ETL Pipeline
    extract_repo(repo_url, local_path)
    file_paths = [f"{local_path}/example_file.txt"]  # Add logic to list actual files
    df = transform_data(file_paths)
    load_data(df, db_url, table_name)

if __name__ == "__main__":
    main()
