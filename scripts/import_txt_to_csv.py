import pandas as pd

print("SCRIPT STARTED")

# File paths
input_path = r"data/raw/CompanyData.txt"
output_path = r"data/processed/CompanyData.csv"

# Read tab-delimited text file
df = pd.read_csv(
    input_path,
    sep="\t",
    header=0,
    encoding='utf-16'
)

# Convert date columns (adjust names if needed)
date_columns = ["Start_Date", "Termination_Date"]

for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], format="%m/%d/%Y")

# Write clean CSV
df.to_csv(output_path, index=False)

print(f"Import complete. Rows:", {len(df)})