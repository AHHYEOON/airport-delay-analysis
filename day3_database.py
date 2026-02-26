import pandas as pd
import sqlite3

df = pd.read_csv("airport_delay_clean.csv", encoding="cp949")

# SQLite DB 만들기 (파일이 없으면 새로 만들어주고, 있으면 연결해주는 코드)
conn = sqlite3.connect("airport_data.db")

# 'delays'라는 이름의 테이블을 만들어서 df를 DB에 넣기
df.to_sql("delays", conn, if_exists="replace", index=False)

# 끝나면 닫아주기
conn.close()