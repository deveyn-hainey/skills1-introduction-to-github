import pandas as pd

def transform_data(file_paths):
    data = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data.append({'file_path': file_path, 'content': file.read()})
    df = pd.DataFrame(data)
    df['line_count'] = df['content'].apply(lambda x: len(x.splitlines()))
    print("Transformation complete")
    return df
