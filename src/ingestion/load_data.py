import pandas as pd
from pathlib import Path


BASE_DATA_PATH = Path("data/raw")


def load_csv(file_name: str) -> pd.DataFrame:
    """
    Generic CSV loader with basic standardisation.
    """
    file_path = BASE_DATA_PATH / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    df = pd.read_csv(file_path)

    return df


def load_customers() -> pd.DataFrame:
    return load_csv("customers.csv")


def load_products() -> pd.DataFrame:
    return load_csv("products.csv")


def load_sales_orders() -> pd.DataFrame:
    df = load_csv("sales_orders.csv")

    # Date parsing
    date_columns = ["order_date", "approval_date", "ship_date"]
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def load_sales_order_items() -> pd.DataFrame:
    return load_csv("sales_order_items.csv")


def load_export_process() -> pd.DataFrame:
    df = load_csv("export_process.csv")

    if "export_date" in df.columns:
        df["export_date"] = pd.to_datetime(df["export_date"], errors="coerce")

    return df


def load_currency_exchange() -> pd.DataFrame:
    df = load_csv("currency_exchange.csv")

    if "rate_date" in df.columns:
        df["rate_date"] = pd.to_datetime(df["rate_date"], errors="coerce")

    return df


def load_all():
    """
    Loads all datasets and returns them as a dictionary.
    """
    return {
        "customers": load_customers(),
        "products": load_products(),
        "sales_orders": load_sales_orders(),
        "sales_order_items": load_sales_order_items(),
        "export_process": load_export_process(),
        "currency_exchange": load_currency_exchange(),
    }


if __name__ == "__main__":
    datasets = load_all()

    for name, df in datasets.items():
        print(f"{name}: {df.shape}")