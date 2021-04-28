import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_data = {rows.letter: rows.code for (index, rows) in data.iterrows()}

def gen_pho():
    usr_inp = input("Enter a word: ").upper()
    try:
        nato_words = [dict_data[i] for i in usr_inp]
    except KeyError:
        print("Please enter only alphabets!")
        gen_pho()
    else:
        print(nato_words)


gen_pho()
