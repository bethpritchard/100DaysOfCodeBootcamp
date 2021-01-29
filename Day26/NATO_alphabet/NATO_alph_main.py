import pandas


df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

def convert():
    word = input("Please input word to convert: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, alphabet only")
        convert()

    else:
        print(output_list)

convert()