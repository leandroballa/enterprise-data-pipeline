import pandas as pd


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