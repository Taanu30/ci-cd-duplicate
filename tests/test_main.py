import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import load_and_process_data

def test_no_duplicates():
    df = load_and_process_data(
        "data/dataset.csv",
        "data/test_output.csv"
    )

    assert df.duplicated().sum() == 0
