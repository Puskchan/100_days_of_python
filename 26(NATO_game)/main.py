import pandas

usr_inp = [letter.upper() for letter in input("Enter a word: ")]

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_data = {rows.letter: rows.code for (index, rows) in data.iterrows()}

nato_words = [dict_data[i] for i in usr_inp if i in dict_data.keys()]

print(nato_words)
