from pyspark.sql import functions as F

def transform(customers, products, transactions):

    # Join all datasets
    df = (
        transactions
        .join(customers, "customer_id", "left")
        .join(products, "product_id", "left")
    )

    # Clean formatting
    df = df.withColumn("city", F.initcap("city"))

    # Add computed column
    df = df.withColumn("total_amount", F.col("quantity") * F.col("price"))

    # Convert timestamp to date + month + year
    df = df.withColumn("date", F.to_date("timestamp"))
    df = df.withColumn("year", F.year("date"))
    df = df.withColumn("month", F.month("date"))

    return df
