def load_clean(df):
    df.write.mode("overwrite").parquet("output/clean")
