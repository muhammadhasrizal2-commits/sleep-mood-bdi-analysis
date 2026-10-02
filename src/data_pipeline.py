from __future__ import annotations

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


def load_raw_data(file_name: str) -> pd.DataFrame:
    """Load a raw CSV file from the project data directory."""
    file_path = RAW_DATA_DIR / file_name
    if not file_path.exists():
        raise FileNotFoundError(f"Raw data file not found: {file_path}")
    return pd.read_csv(file_path)


def save_processed_data(df: pd.DataFrame, file_name: str) -> Path:
    """Write a cleaned DataFrame to the processed data directory."""
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA_DIR / file_name
    df.to_csv(output_path, index=False)
    return output_path


def describe_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a concise schema summary for a DataFrame."""
    return pd.DataFrame(
        {
            "column": df.columns,
            "dtype": [str(dtype) for dtype in df.dtypes],
            "null_count": df.isnull().sum().to_numpy(),
        }
    )
