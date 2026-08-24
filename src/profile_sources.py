from pathlib import Path
import pandas as pd
import json

RAW = Path("data/raw")

def make_hashable(value):
    """Convert dict/list to JSON string to make it hashable for pandas operations."""
    if isinstance(value, (dict, list)):
        return json.dumps(value, sort_keys=True, default=str)
    return value

def safe_parse_dates(series):
    """Try to parse a series as datetime. Return parsed series if at least 50% values are valid dates."""
    parsed = pd.to_datetime(series, errors="coerce")
    if parsed.notna().sum() > len(parsed) * 0.5:
        return parsed
    return None

def profile_dataframe(df, file_name):
    print(f"\n{'='*60}")
    print(f"FILE: {file_name}")
    print(f"{'='*60}")

    file_path = RAW / file_name
    if file_path.exists():
        size_bytes = file_path.stat().st_size
        size_kb = size_bytes / 1024
        print(f"File size: {size_bytes} bytes ({size_kb:.2f} KB)")
    else:
        print(f"File not found at {file_path}, size unknown")

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn names (original order):")
    for col in df.columns:
        print(f"  - {col}")

    print("\nInferred data types:")
    for col, dtype in df.dtypes.items():
        print(f"  - {col}: {dtype}")

    # Detect nested columns and create hashable copy for duplicate/distinct analysis
    print("\nNested structure detection:")
    df_hashable = df.copy()
    nested_cols = []
    for col in df.columns:
        if df[col].dtype == object:
            has_nested = df[col].apply(lambda x: isinstance(x, (dict, list))).any()
            if has_nested:
                nested_cols.append(col)
                print(f"  - Column '{col}' contains nested objects/lists. Converting to JSON strings for duplicate/distinct analysis.")
                df_hashable[col] = df[col].apply(make_hashable)
    if not nested_cols:
        print("  - No nested objects/lists detected.")

    print("\nMissing values per column:")
    missing = df.isna().sum()
    for col, count in missing.items():
        print(f"  - {col}: {count}")

    print(f"\nFully duplicated rows: {df_hashable.duplicated().sum()}")

    print("\nDistinct values per column:")
    for col in df.columns:
        nunique = df_hashable[col].nunique(dropna=True)
        print(f"  - {col}: {nunique} distinct")

    print("\nFirst five records:")
    print(df.head().to_string(index=False))

    numeric_cols = df.select_dtypes(include=["number"]).columns
    if len(numeric_cols) > 0:
        print("\nNumeric column min/max:")
        for col in numeric_cols:
            col_min = df[col].min()
            col_max = df[col].max()
            print(f"  - {col}: min={col_min}, max={col_max}")
    else:
        print("\nNo numeric columns found.")

    print("\nDate/time-like columns (earliest/latest):")
    found_date = False
    for col in df.columns:
        if df[col].dtype == "object":
            parsed_dates = safe_parse_dates(df[col])
            if parsed_dates is not None:
                earliest = parsed_dates.min()
                latest = parsed_dates.max()
                print(f"  - {col}: earliest={earliest}, latest={latest}")
                found_date = True
    if not found_date:
        print("  - No date/time-like columns detected.")

def main():
    csv_path = RAW / "customers.csv"
    if csv_path.exists():
        customers_df = pd.read_csv(csv_path)
        profile_dataframe(customers_df, "customers.csv")
    else:
        print(f"customers.csv not found at {csv_path}")

    json_path = RAW / "orders.json"
    if json_path.exists():
        orders_df = pd.read_json(json_path)
        profile_dataframe(orders_df, "orders.json")
    else:
        print(f"orders.json not found at {json_path}")

    parquet_path = RAW / "products.parquet"
    if parquet_path.exists():
        products_df = pd.read_parquet(parquet_path)
        profile_dataframe(products_df, "products.parquet")
    else:
        print(f"products.parquet not found at {parquet_path}")

if __name__ == "__main__":
    main()