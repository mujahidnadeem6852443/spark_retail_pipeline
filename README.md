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


mermaid
flowchart TD
    A[CSV Input Files] --> B[PySpark Extract]
    B --> C[Transform Layer]
    C --> D[Clean Parquet Data]
    C --> E[Analytics Layer]
    E --> F[Insights CSV Output]



# 🔥 **ALL FILES ARE NOW READY.**

Now we go into the **Git workflow**.

---

# ✅ **PART 2 — PROFESSIONAL GIT WORKFLOW (STARTING FROM YOUR CURRENT STATE)**

You are currently on **main**, and the project is already pushed.

Follow these EXACT commands in order.

---

# ⭐ **STEP 1 — Create the dev branch**

```bash
git checkout -b dev
git push -u origin dev


## Future Improvements
- Add CI/CD pipeline