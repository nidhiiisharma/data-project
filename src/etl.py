import pandas as pd

print("Starting ETL pipeline...")

# Extract
df = pd.read_csv("data/data.csv")
print("Extracted raw CSV data")

# Transform
print("Transforming data...")

if "product" in df.columns:
    df["product"] = df["product"].astype(str).str.strip()

# Convert date column to proper datetime
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Remove rows with missing values
df = df.dropna(subset=["quantity", "price"])

# Remove invalid values
df = df[(df["quantity"] > 0) & (df["price"] > 0)]

# Add a new total column
df["total"] = df["quantity"] * df["price"]

print("Transform complete")

# Load
# Save the cleaned data into a new CSV file
print("Loading data...")
df.to_csv("data/clean_data.csv", index=False)
print("Loaded cleaned data to data/clean_data.csv")

print("ETL pipeline complete.")