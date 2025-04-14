# Convert a CSV file to a Parquet file.
import pandas as pd

# Read CSV file into a DataFrame
df = pd.read_csv("data/sample.csv")

# Write the DataFrame to a Parquet file, excluding the index if specified
df.to_parquet("data/sample.parquet", index=False)