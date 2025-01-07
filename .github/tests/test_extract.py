from etl.extract import extract_repo

def test_extract_repo():
    assert extract_repo is not None  # Simple existence test
