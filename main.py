import pandas as pd

df = pd.read_csv("airport_delay.csv", encoding = "cp949")

# 불러온 데이터의 첫 5줄만 화면에 출력
print(df.head())

print(df.columns)

# 데이터에 빈칸(결측치)는 없는지 데이터 타입은 무엇인지 요약본 보기
print(df.info())

# 변경 전 컬럼명 확인
print("변경 전:", df.columns)

# 컬럼명에 있는 모든 공백(' ')을 빈칸('')으로 모두 바꾸기
df.columns = df.columns.str.replace(' ','')

# 변경 후 컬럼명 확인
print("\n변경 후:", df.columns)

# 데이터 새로운 이름의 csv 파일로 저장하기
df.to_csv("airport_delay_clean.csv", index = False, encoding="cp949")