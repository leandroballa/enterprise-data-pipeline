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