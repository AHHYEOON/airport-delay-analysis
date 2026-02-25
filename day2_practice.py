import pandas as pd

df = pd.read_csv("airport_delay_clean.csv", encoding="cp949")

best_count = df.groupby('연도')['운항'].sum()

sorted_count = best_count.sort_values(ascending=False)

print(sorted_count.head())