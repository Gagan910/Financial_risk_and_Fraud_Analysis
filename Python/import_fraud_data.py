from urllib.parse import quote_plus
import pandas as pd
from sqlalchemy import create_engine

print("RUNNING UPDATED SCRIPT WITH analytics_user")

password = quote_plus("analytics123")

engine = create_engine(
    f"mysql+pymysql://analytics_user:{password}@localhost:3306/financial_fraud"
)

df = pd.read_csv("data/fraudTest.csv")

print("CSV loaded. Rows:", len(df))

df.to_sql(
    name="fraud_transactions",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=5000
)

print("IMPORT COMPLETED SUCCESSFULLY")
