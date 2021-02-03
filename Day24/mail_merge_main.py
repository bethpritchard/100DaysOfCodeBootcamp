PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


for i in range(len(names)):
    names[i] = names[i].replace('\n', " ")
    names[i] = names[i].strip()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for name in names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as new_letter:
        letter = letter.replace(PLACEHOLDER, name)
        letter = letter.replace("Angela", "Beth")
        new_letter.write(f"{letter}")