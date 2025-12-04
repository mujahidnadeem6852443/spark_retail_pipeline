from etl.extract import get_spark, extract_data
from etl.transform import transform
from etl.load import load_clean
from etl.analytics import run_analytics
from etl.utils import log

def main():
    log("Starting PySpark ETL Pipeline...")

    spark = get_spark()

    log("Extracting data...")
    customers, products, transactions = extract_data(spark)

    log("Transforming data...")
    df = transform(customers, products, transactions)

    df.cache()

    log("Loading cleaned dataset as parquet...")
    load_clean(df)

    log("Running analytics...")
    revenue_by_city, top_products, monthly_revenue = run_analytics(df)

    log("Saving analytics output...")
    revenue_by_city.write.mode("overwrite").csv("output/insights/revenue_by_city", header=True)
    top_products.write.mode("overwrite").csv("output/insights/top_products", header=True)
    monthly_revenue.write.mode("overwrite").csv("output/insights/monthly_revenue", header=True)

    log("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
