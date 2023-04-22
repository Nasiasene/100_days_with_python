with open("/Users/davit/Documents/100days_python.py/100_days_with_python/codes/day24/Input/Names/list_names.txt") as name_list:
    names = name_list.readlines()


with open("/Users/davit/Documents/100days_python.py/100_days_with_python/codes/day24/Input/Letters/letter.txt") as text:
    letter = text.read()
    for i in names:
        i = i.strip("\n")
        new_letter = letter.replace("[name]", f"{i}")
        with open(f"/Users/davit/Documents/100days_python.py/100_days_with_python/codes/day24/Output/ReadToSend/letter_to_{i.lower()}.txt", mode = 'a') as finish_letter:
            finish_letter.write(new_letter)
