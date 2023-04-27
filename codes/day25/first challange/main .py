import pandas as pd

csv = 'weather_data.csv'
df = pd.read_csv(csv)
max_temp = df['temp'].max()
print(df[df['temp'] == 24])

print("\n", "*"*70, "\n")

md = df[df['day'] == 'Monday']
temp_f = float(md['temp'] * (9/5) + 32)
print(temp_f)

