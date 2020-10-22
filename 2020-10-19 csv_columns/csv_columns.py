import csv
from collections import defaultdict
from typing import TextIO


def csv_columns(file: TextIO, headers: list = None, missing: str = None) -> dict:
    reader = csv.DictReader(
        file, 
        fieldnames=headers, 
        restval=missing
    )

    columns = defaultdict(list)

    for row in reader:
        for key, value in row.items():
            columns[key].append(value)
    
    return columns
