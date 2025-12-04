from pyspark.sql import SparkSession

def get_spark():
    spark = (
        SparkSession.builder
        .appName("RetailSparkETL")
        .master("local[*]")  # FREE local Spark mode
        .getOrCreate()
    )
    return spark

def extract_data(spark):
    customers = spark.read.csv("data/customers.csv", header=True, inferSchema=True)
    products = spark.read.csv("data/products.csv", header=True, inferSchema=True)
    transactions = spark.read.csv("data/transactions.csv", header=True, inferSchema=True)
    return customers, products, transactions
