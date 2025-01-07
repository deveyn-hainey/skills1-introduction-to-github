import os
from etl.extract import extract_repo

def test_extract_repo(tmp_path):
    repo_url = "https://github.com/example/example-repo.git"
    local_path = tmp_path / "repo"
    
    # Run extract function
    extract_repo(repo_url, local_path)
    
    # Assert that repo files exist
    assert os.path.exists(local_path / ".git")
