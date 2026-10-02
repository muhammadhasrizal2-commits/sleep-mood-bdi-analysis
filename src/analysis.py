from __future__ import annotations

from pathlib import Path

from src.data_pipeline import PROJECT_ROOT, describe_columns, load_raw_data


def main() -> None:
    """Run the initial project sanity check."""
    print(f"Project root: {PROJECT_ROOT}")
    raw_dir = PROJECT_ROOT / "data" / "raw"
    csv_files = sorted(raw_dir.glob("*.csv")) if raw_dir.exists() else []
    if not csv_files:
        print("No raw CSV files found yet. Add CSV files to data/raw/ to begin analysis.")
        return

    first_file = csv_files[0]
    df = load_raw_data(first_file.name)
    print(f"Loaded dataset: {first_file.name} ({len(df)} rows, {len(df.columns)} columns)")
    print(describe_columns(df).to_string(index=False))


if __name__ == "__main__":
    main()
