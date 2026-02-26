import pandas as pd
import sqlite3

conn = sqlite3.connect("airport_data.db")

query = "SELECT * FROM delays WHERE 공항 = 'CJU'"

result_df = pd.read_sql(query, conn)

print("\n=== DB에서 SQL로 직접 꺼내온 제주공항 데이터 ===")
print(result_df.head())

conn.close()