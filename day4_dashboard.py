import streamlit as st
import pandas as pd
import sqlite3

# 웹 페이지 제목 설정
st.title("전국 공항 지연 데이터 데시보드")
st.write("SQLite DB에서 데이터를 가져와서 띄워주는 웹사이트입니다")

conn = sqlite3.connect("airport_data.db")
# 모든 공항의 기상 지연 데이터를 가져오는 쿼리
query = "SELECT 공항, 기상 FROM delays" 
df = pd.read_sql(query, conn)
conn.close()

# 데이터 가공 (전국 공항별 기상 지연 총합)
airport_group = df.groupby('공항')['기상'].sum().sort_values(ascending=False)

# 화면에 그리기
st.subheader("전국 공항별 기상 지연 순위(표)")
st.dataframe(airport_group)

st.subheader("한눈에 보는 막대그래프")
st.bar_chart(airport_group)

