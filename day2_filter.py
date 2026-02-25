import pandas as pd

df = pd.read_csv("airport_delay_clean.csv", encoding="cp949")

# '공항' 컬럼이 'CJU'(제주공항)인 데이터만 골라서 새로운 변수에 담기 
jeju_df = df[df['공항'] == 'CJU']

print("===제주공항 데이터===")
print(jeju_df.head())

# 숫자 조건으로 필터링: 제주공항 데이터 중 '기상' 지연이 100건 이상인 해만 필터링
severe_weather_df = jeju_df[jeju_df['기상'] >= 100]
print("\n=== 기상 지연 100건 이상인 제주공항 데이터 ===")
print(severe_weather_df[['연도', '운항', '기상']])

# 데이터 줄 세우기(정렬)
sorted_jeju = jeju_df.sort_values(by='기상', ascending =False)

print("\n=== 기상 지연 최악의 해 Top 3 ===")
print(sorted_jeju[['연도','기상']].head(3))

airport_ranking = df.groupby('공항')['기상'].sum()

print("\n=== 전국 공항별 기상 악화 지연 랭킹 ===")
print(airport_ranking)