import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in df.iterrows()}


user_input = str(input("Please input word to convert: ")).upper()

user_list = [letter for letter in user_input]


print([code for (letter, code) in alphabet.items() if letter in user_list])