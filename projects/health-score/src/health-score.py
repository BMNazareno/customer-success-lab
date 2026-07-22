from pathlib import Path
import pandas as pd


def main():
    base_path = Path(__file__).parent.parent
    csv_path = base_path / "data" / "clientes.csv"

    df = pd.read_csv(csv_path)

    print(df)


if __name__ == "__main__":
    main() 