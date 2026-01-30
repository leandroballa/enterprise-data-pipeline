from src.ingestion.load_data import load_all
from src.validation.business_rules import (
    validate_export_status_consistency,
    validate_order_total_value,
    validate_currency_conversion_rate,
    validate_export_cost_threshold,
    validate_shipping_performance_kpi,
    validate_customer_active_status
)

def main():
    data = load_all()

    invalid_exports = validate_export_status_consistency(
        sales_orders=data["sales_orders"],
        export_process=data["export_process"]
    )

    print("\nInvalid export status records:")
    print(invalid_exports)

    invalid_order_values = validate_order_total_value(
        sales_orders=data["sales_orders"],
        sales_order_items=data["sales_order_items"]
    )

    print("\nInvalid export status records:")
    print(invalid_exports)

    print("\nInvalid order total value records:")
    print(invalid_order_values)

    invalid_currency_conversion = validate_currency_conversion_rate(
        sales_orders=data["sales_orders"],
        currency_rates=data["currency_rates"]
    )

    print("\nInvalid currency conversion rate records:")
    print(invalid_currency_conversion)

    invalid_export_costs = validate_export_cost_threshold(
        sales_orders=data["sales_orders"],
        sales_order_items=data["sales_order_items"],
        export_process=data["export_process"]
    )

    print("\nInvalid export cost threshold records:")
    print(invalid_export_costs)

    invalid_shipping_performance = validate_shipping_performance_kpi(
        sales_orders=data["sales_orders"],
        export_process=data["export_process"]
    )

    print("\nInvalid shipping performance KPI records:")
    print(invalid_shipping_performance)

    invalid_customer_status = validate_customer_active_status(
        sales_orders=data["sales_orders"],
        customers=data["customers"]
    )

    print("\nInvalid customer active status records:")
    print(invalid_customer_status)
    
    sales_orders_totals = sales_orders.merge(
        sales_order_items.groupby("order_id")["item_total"].sum().reset_index(),
        on="order_id",
        how="left"
    )

    print("\nSales Orders with Total Values:")
    print(sales_orders_totals)

if __name__ == "__main__":
    main()