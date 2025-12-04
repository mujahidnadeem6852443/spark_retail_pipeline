from pyspark.sql import functions as F

def run_analytics(df):

    # Total revenue by city
    revenue_by_city = (
        df.groupBy("city")
        .agg(F.sum("total_amount").alias("city_revenue"))
        .orderBy(F.desc("city_revenue"))
    )

    # Top products
    top_products = (
        df.groupBy("name")
        .agg(
            F.sum("total_amount").alias("product_revenue"),
            F.sum("quantity").alias("total_units_sold")
        )
        .orderBy(F.desc("product_revenue"))
    )

    # Monthly revenue trend
    monthly_revenue = (
        df.groupBy("year", "month")
        .agg(F.sum("total_amount").alias("monthly_revenue"))
        .orderBy("year", "month")
    )

    return revenue_by_city, top_products, monthly_revenue
