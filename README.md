# Spark Retail ETL & Analytics Pipeline

A fully local, free-to-run PySpark ETL project using real retail datasets.  
No cluster, no cloud, no Hadoop required. Runs entirely in PySpark local mode.

## Features
- Extracts customers, products, and transaction data
- Transformations include joins, cleaning, computed fields, date parsing
- Outputs cleaned data as Parquet
- Analytical queries using Spark:
  - Revenue by city
  - Top products by revenue
  - Monthly revenue trends
- Exports insights to CSV

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the pipeline:
   python main.py

## Output
- Clean parquet dataset: output/clean/
- Insight reports (CSV): output/insights/
