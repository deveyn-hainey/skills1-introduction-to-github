import pandas as pd
from etl.transform import transform_data

def test_transform_data(tmp_path):
    file_paths = [tmp_path / "test_file_1.txt", tmp_path / "test_file_2.txt"]
    
    # Create dummy files
    for file_path in file_paths:
        with open(file_path, 'w') as file:
            file.write("Line 1\nLine 2\nLine 3")
    
    # Run transform function
    df = transform_data(file_paths)
    
    # Assert transformations
    assert isinstance(df, pd.DataFrame)
    assert all(df['line_count'] == 3)

