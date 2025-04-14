from server import mcp
from utils.file_reader import summarize_parquet

@mcp.tool()
def summarize_parquet_file(filename: str) -> str:
    """
    Provides a summary of a Parquet file by determining its row and column counts.

    Parameters:
        filename (str): The name of the Parquet file stored in the /data folder (e.g., 'sample.parquet').

    Returns:
        str: A brief description detailing the dimensions of the file.
    """
    return summarize_parquet(filename)