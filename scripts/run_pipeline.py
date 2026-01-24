from src.ingestion.load_data import load_all
from src.validation.business_rules import validate_export_status_consistency

def main():
    data = load_all()

    invalid_exports = validate_export_status_consistency(
        sales_orders=data["sales_orders"],
        export_process=data["export_process"]
    )

    print("Invalid export status records:")
    print(invalid_exports)

if __name__ == "__main__":
    main()