names_array = []

with open('Names/invited_names.txt', mode='r') as file:
    names_array = file.read().split('\n')
with open('Letters/starting_letter.txt', mode='r') as file:
    letter = file.read()


for name in names_array:
    with open(f'Letters/letter_for_{name}.txt', mode='w') as file:
        new_letter = letter.replace('[name]', name)
        file.write(new_letter)
