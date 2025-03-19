import os
import pandas as pd

def test_csv_exists():
    """Test if the results CSV file is generated and not empty."""
    csv_path = os.path.join("results", "simulation_results.csv")
    assert os.path.exists(csv_path), "simulation_results.csv does not exist!"
    df = pd.read_csv(csv_path)
    assert not df.empty, "CSV file is empty!"

if __name__ == "__main__":
    test_csv_exists()
