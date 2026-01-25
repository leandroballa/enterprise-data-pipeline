# Automated generation of data for the project
import pandas as pd
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

BASE_PATH = PROJECT_ROOT / "data" / "raw"
BASE_PATH.mkdir(parents=True, exist_ok=True)

# Customers
customers = pd.DataFrame([
    [1, "Renner Argentina", "AR", "B2B"],
    [2, "Renner Uruguay", "UY", "B2B"],
    [3, "International Retail Partner", "US", "B2B"],
], columns=["customer_id", "customer_name", "country", "customer_type"])

customers.to_csv(BASE_PATH / "customers.csv", index=False)

# Products
products = pd.DataFrame([
    [101, "T-Shirt Basic", "Apparel", 15.00, "USD"],
    [102, "Jeans Slim", "Apparel", 45.00, "USD"],
    [103, "Sneakers Casual", "Footwear", 60.00, "USD"],
], columns=["product_id", "product_name", "category", "unit_price", "currency"])

products.to_csv(BASE_PATH / "products.csv", index=False)

# Sales Orders
orders = pd.DataFrame([
    [1001, 1, "2024-01-05", "2024-01-06", "2024-01-10", "AR", "SHIPPED"],
    [1002, 2, "2024-01-08", "2024-01-09", None, "UY", "APPROVED"],
    [1003, 3, "2024-01-10", "2024-01-11", "2024-01-25", "US", "SHIPPED"],
], columns=[
    "order_id", "customer_id", "order_date",
    "approval_date", "ship_date",
    "country_destination", "order_status"
])

orders.to_csv(BASE_PATH / "sales_orders.csv", index=False)

# Order Items
items = pd.DataFrame([
    [1, 1001, 101, 100, 15.00],
    [2, 1001, 102, 50, 45.00],
    [3, 1002, 101, 20, 15.00],
    [4, 1003, 103, 10, 60.00],
], columns=["order_item_id", "order_id", "product_id", "quantity", "unit_price"])

items.to_csv(BASE_PATH / "sales_order_items.csv", index=False)

# Export Process
exports = pd.DataFrame([
    [5001, 1001, "AR", "2024-01-11", "SHIPPED", 900.00],
    [5002, 1002, "UY", "2024-01-12", "SHIPPED", 300.00],
    [5003, 1003, "US", "2024-01-26", "SHIPPED", 2000.00],
], columns=[
    "export_id", "order_id", "export_country",
    "export_date", "export_status", "export_cost"
])

exports.to_csv(BASE_PATH / "export_process.csv", index=False)

# Currency Exchange
currency = pd.DataFrame([
    ["USD", 1.00, "2024-01-05"],
    ["ARS", 0.0012, "2024-01-05"],
    ["UYU", 0.026, "2024-01-08"],
], columns=["currency", "exchange_rate_to_usd", "rate_date"])

currency.to_csv(BASE_PATH / "currency_exchange.csv", index=False)

print("CSV files successfully generated.")