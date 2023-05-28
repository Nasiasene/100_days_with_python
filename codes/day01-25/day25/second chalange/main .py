import pandas as pd

df = pd.read_csv("Squirrel_Data.csv")
dict = df['Primary Fur Color'].value_counts().to_dict()
new_df =  pd.DataFrame(dict, index = [0])
new_df.to_csv("colors_count.csv")
print(new_df)