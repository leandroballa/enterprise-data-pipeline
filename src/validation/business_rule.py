import pandas as pd

# First Rule
def validate_export_status_consistency(
    sales_orders: pd.DataFrame,
    export_process: pd.DataFrame
) -> pd.DataFrame:
    """
    Validates that only shipped sales orders
    can have export_status = 'SHIPPED'.
    """

    merged_df = sales_orders.merge(
        export_process,
        on="order_id",
        how="inner",
        suffixes=("_order", "_export")
    )

    invalid_exports = merged_df[
        (merged_df["export_status"] == "SHIPPED") &
        (merged_df["order_status"] != "SHIPPED")
    ].copy()

    invalid_exports["validation_error"] = (
        "Export marked as SHIPPED while sales order is not SHIPPED"
    )

    return invalid_exports[
        [
            "order_id",
            "order_status",
            "export_status",
            "validation_error"
        ]
    ]

# Second Rule
def validate_order_total_value(
    sales_orders: pd.DataFrame,
    sales_order_items: pd.DataFrame
) -> pd.DataFrame:
    """
    Validates that every sales order has a total value greater than zero.
    """

    # Calculate total order value
    order_totals = (
        sales_order_items
        .assign(total_value=lambda df: df["quantity"] * df["unit_price"])
        .groupby("order_id", as_index=False)["total_value"]
        .sum()
    )

    # Join with sales orders to ensure all orders are evaluated
    merged_df = sales_orders.merge(
        order_totals,
        on="order_id",
        how="left"
    )

    # Orders without items will have NaN total_value
    merged_df["total_value"] = merged_df["total_value"].fillna(0)

    invalid_orders = merged_df[
        merged_df["total_value"] <= 0
    ].copy()

    invalid_orders["validation_error"] = (
        "Sales order total value must be greater than zero"
    )

    return invalid_orders[
        [
            "order_id",
            "total_value",
            "validation_error"
        ]
    ]

# Third Rule
def validate_currency_conversion_rate(
    sales_orders: pd.DataFrame,
    currency_rates: pd.DataFrame
) -> pd.DataFrame:
    """
    Validates that sales orders in foreign currencies
    have a valid conversion rate.
    """

    merged_df = sales_orders.merge(
        currency_rates,
        on=["currency_code", "order_date"],
        how="left",
        suffixes=("_order", "_rate")
    )

    invalid_currency_orders = merged_df[
        (merged_df["currency_code"] != "USD") &
        (merged_df["conversion_rate"].isna() |
         (merged_df["conversion_rate"] <= 0))
    ].copy()

    invalid_currency_orders["validation_error"] = (
        "Invalid or missing currency conversion rate for foreign currency order"
    )

    return invalid_currency_orders[
        [
            "order_id",
            "currency_code",
            "order_date",
            "conversion_rate",
            "validation_error"
        ]
    ]

# Fourth Rule

# Fifth Rule

# Sixth Rule
def validate_customer_active_status(
    sales_orders: pd.DataFrame,
    customers: pd.DataFrame
) -> pd.DataFrame:
    """
    Validates that sales orders are only created for active customers.
    """

    merged_df = sales_orders.merge(
        customers,
        on="customer_id",
        how="inner",
        suffixes=("_order", "_customer")
    )

    invalid_customers = merged_df[
        merged_df["is_active"] == False
    ].copy()

    invalid_customers["validation_error"] = (
        "Sales order created for inactive customer"
    )

    return invalid_customers[
        [
            "order_id",
            "customer_id",
            "is_active",
            "validation_error"
        ]
    ]