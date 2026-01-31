import pandas as pd

def run_data_quality_checks(
    sales_orders: pd.DataFrame,
    sales_order_items: pd.DataFrame,
    export_process: pd.DataFrame,
    currency_rates: pd.DataFrame,
    customers: pd.DataFrame
) -> pd.DataFrame:
    """
    Executes all data quality and KPI validation rules
    and returns a consolidated report.
    """

    results = []

    # Rule 1
    from .business_rules import validate_export_status_consistency
    df = validate_export_status_consistency(
        sales_orders, export_process
    )
    if not df.empty:
        df["rule_name"] = "Export Status Consistency"
        df["severity"] = "ERROR"
        results.append(df)

    # Rule 2
    from .business_rules import validate_order_total_value
    df = validate_order_total_value(
        sales_orders, sales_order_items
    )
    if not df.empty:
        df["rule_name"] = "Order Total Value"
        df["severity"] = "ERROR"
        results.append(df)

    # Rule 3
    from .business_rules import validate_currency_conversion_rate
    df = validate_currency_conversion_rate(
        sales_orders, currency_rates
    )
    if not df.empty:
        df["rule_name"] = "Currency Conversion Rate"
        df["severity"] = "ERROR"
        results.append(df)

    # Rule 4
    from .business_rules import validate_export_cost_threshold
    df = validate_export_cost_threshold(
        sales_orders, sales_order_items, export_process
    )
    if not df.empty:
        df["rule_name"] = "Export Cost Threshold"
        df["severity"] = "ERROR"
        results.append(df)

    # Rule 5 (KPI)
    from .business_rules import validate_shipping_performance_kpi
    df = validate_shipping_performance_kpi(
        sales_orders, export_process
    )
    if not df.empty:
        df["rule_name"] = "Shipping Performance SLA"
        df["severity"] = "KPI"
        results.append(df)

    # Rule 6
    from .business_rules import validate_customer_active_status
    df = validate_customer_active_status(
        sales_orders, customers
    )
    if not df.empty:
        df["rule_name"] = "Customer Active Status"
        df["severity"] = "ERROR"
        results.append(df)

    if not results:
        return pd.DataFrame()

    return pd.concat(results, ignore_index=True)