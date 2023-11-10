names_array = []

with open('Names/invited_names.txt', mode='r') as file:
    names = file.read()
    names_array = names.split('\n')
with open('Letters/starting_letter.txt', mode='r') as file:
    letter = file.read()

print(names_array)
print(len(names_array))

for name in names_array:
    with open(f'Letters/letter_for_{name}.txt', mode='w') as file:
        new_letter = letter.replace('[name]', name)
        file.write(new_letter)
