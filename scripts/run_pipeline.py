from src.ingestion.load_data import load_all
from src.validation.business_rules import (
    validate_export_status_consistency,
    validate_order_total_value
)

def main():
    data = load_all()

    invalid_exports = validate_export_status_consistency(
        sales_orders=data["sales_orders"],
        export_process=data["export_process"]
    )

    invalid_order_values = validate_order_total_value(
        sales_orders=data["sales_orders"],
        sales_order_items=data["sales_order_items"]
    )

    print("\nInvalid export status records:")
    print(invalid_exports)

    print("\nInvalid order total value records:")
    print(invalid_order_values)

if __name__ == "__main__":
    main()