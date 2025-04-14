import pandas as pd
from pathlib import Path

# Establish the base directory where our data files are stored
BASE_DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def summarize_csv(file_name: str) -> str:
    """
    Load a CSV file and generate a concise summary.
    
    Parameters:
        file_name (str): The name of the CSV file (e.g., 'data.csv').
    
    Returns:
        str: A description indicating the number of rows and columns.
    """
    path_to_file = BASE_DATA_DIR / file_name
    data_frame = pd.read_csv(path_to_file)
    rows, columns = len(data_frame), len(data_frame.columns)
    return f"CSV file '{file_name}' contains {rows} rows and {columns} columns."

def summarize_parquet(file_name: str) -> str:
    """
    Load a Parquet file and generate a concise summary.
    
    Parameters:
        file_name (str): The name of the Parquet file (e.g., 'data.parquet').
    
    Returns:
        str: A description indicating the number of rows and columns.
    """
    path_to_file = BASE_DATA_DIR / file_name
    data_frame = pd.read_parquet(path_to_file)
    rows, columns = len(data_frame), len(data_frame.columns)
    return f"Parquet file '{file_name}' contains {rows} rows and {columns} columns."