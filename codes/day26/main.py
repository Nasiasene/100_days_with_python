import pandas as pd


df = pd.read_csv("NATO_alphabet.csv")


new_dict = {row['letter']:row['code'] for (index, row) in df.iterrows()}


word = input("Insert a word: ").upper()
new_list = [new_dict[n] for n in word]
print(new_list)