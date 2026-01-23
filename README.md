## Enterprise Data Extraction & Analysis Pipeline

This project demonstrates a Python-based data pipeline designed to extract, validate, analyse, and export data from relational databases in an enterprise context.

# 📦 Retail Export & Integration Data Project

## 📌 Project Overview
This project simulates a **real-world retail export operation**, focusing on **data analysis, business rule validation, and enterprise system integrations**.

The dataset represents typical interactions between:
- ERP systems (e.g. Oracle EBS)
- Retail systems (e.g. Oracle Retail)
- Foreign trade platforms (e.g. Ecomex)

The primary goal is to demonstrate **data modelling, data quality validation, analytical processing, and performance-oriented solutions using Python**.

---

## 🏗️ Data Model Overview
The dataset is structured to reflect real transactional and operational flows and includes the following entities:

- **Customers**
- **Products**
- **Sales Orders**
- **Sales Order Items**
- **Export Process**
- **Currency Exchange Rates**

These entities are related to allow realistic joins, aggregations, validations, and performance analysis across systems.

---

## 🧠 Business Rules

### 1️⃣ Export Status Consistency
Only sales orders that have been physically shipped can be marked as exported.

**Rule:**
If sales_order.order_status != ‘SHIPPED’
then export_process.export_status != ‘SHIPPED’

**Purpose:**  
Ensures consistency between operational and export systems, identifying integration or process failures.

---

### 2️⃣ Order Value Validation
Every sales order must have a valid financial value.

**Rule:**
Total Order Value = SUM(quantity × unit_price)
Total Order Value must be greater than zero

**Purpose:**  
Prevents invalid financial records and supports accurate financial reporting.

---

### 3️⃣ Currency Conversion
All financial analysis and reports are standardised in **USD**.

**Rule:**
Order values must be converted to USD
using the exchange rate from the order date

**Purpose:**  
Ensures consistent financial analysis across countries and currencies.

---

### 4️⃣ Export Cost Threshold
Export-related operational costs must remain within an acceptable margin.

**Rule:**
Export cost must not exceed 20% of the total order value

**Purpose:**  
Supports cost control, margin analysis, and operational efficiency monitoring.

---

### 5️⃣ Shipping Performance KPI
Measures operational efficiency between order approval and shipment.

**Rule:**
Orders must be shipped within 5 days after approval

**Purpose:**  
Enables SLA-style monitoring and logistics performance analysis.

---

## 📊 Analytical Outputs

### Key Performance Indicators (KPIs)
- Total export value (USD)
- Export cost ratio (%)
- Average shipping time
- Number of orders per destination country

### Data Quality & Validation Reports
- Orders with inconsistent or invalid statuses
- Missing or invalid exchange rates
- Export costs exceeding defined thresholds

---

## 🛠️ Technologies & Tools
- **Python** (Pandas, NumPy)
- **SQL** (data extraction and transformations)
- **Git & GitHub**
- **VS Code**
- CSV-based datasets (simulating ERP and integration outputs)

---

## 🎯 Project Objectives
This project demonstrates:
- Enterprise-level data modelling
- Business rule enforcement
- Data quality and validation strategies
- Financial and operational analytics
- Integration-oriented data thinking

---

## 🔮 Future Enhancements
- API-based data ingestion
- Cloud-oriented data storage simulation
- Interactive dashboards
- Performance optimisation for large datasets
- Event-driven integration scenarios

---

## 📎 Disclaimer
All data used in this project is **synthetic and anonymised**, created exclusively for educational and demonstration purposes.