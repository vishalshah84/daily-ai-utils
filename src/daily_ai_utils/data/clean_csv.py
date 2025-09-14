import pandas as pd
from pathlib import Path

def clean_csv(input_path: str, output_path: str | None = None) -> str:
    """
    Clean a CSV file by dropping empty rows and duplicate rows.
    Returns the path to the cleaned file.
    """
    df = pd.read_csv(input_path)

    # drop completely empty rows
    df.dropna(how="all", inplace=True)

    # drop duplicate rows
    df.drop_duplicates(inplace=True)

    if output_path is None:
        output_path = str(Path(input_path).with_name(Path(input_path).stem + "_clean.csv"))

    df.to_csv(output_path, index=False)
    return output_path
