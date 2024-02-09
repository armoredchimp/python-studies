import pandas
import csv

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# with open('nato_phonetic_alphabet.csv', newline='') as csvfile:

#     nato_doc = csv.reader(csvfile, delimiter=',', quotechar='|')
#     nato_alph = {letter: code for letter, code in nato_doc}


# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# user_input = input('Type something: ').upper()
# letters = [nato_alph[char] for char in user_input if char in nato_alph]
# print(letters)

data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def get_input():
    user_input = input('Type something: ').upper()
    try:
        letters = [phonetic_dict[letter] for letter in user_input]
        print(letters)
    except KeyError:
        print('Invalid Input')
        get_input()


get_input()

# student_data_frame = pandas.DataFrame(student_dict)

# for (index, row) in student_data_frame.iterrows():
#     print(row)
#     print(row.score)
#     if row.student == 'Maurizio':
#         print(row.score - 20)
