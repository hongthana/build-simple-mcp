from server import mcp
from utils.file_reader import summarize_csv

@mcp.tool()
def summarize_csv_file(filename: str) -> str:
    """
    Generates a summary of a CSV file by counting its rows and columns.

    Parameters:
        filename (str): The name of the CSV file located in the /data directory (e.g., 'sample.csv').

    Returns:
        str: A description outlining the dimensions of the CSV file.
    """
    return summarize_csv(filename)