import pandas as pd


df = pd.read_csv("NATO_alphabet.csv")


new_dict = {row['letter']:row['code'] for (index, row) in df.iterrows()}


def generate_word():
    word = input("Insert a word: ").upper()
    try:
        new_list = [new_dict[n] for n in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_word()
    else:
        print(new_list)

generate_word()