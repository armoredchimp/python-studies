import random

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)


doubled_nums = [n*2 for n in range(1, 5)]
print(doubled_nums)


# Conditional List Comprehension
names = ['Bill', 'Ted', 'Marcus', 'Samantha', 'Angela', 'Sally']
short_names = [name for name in names if len(name) <= 4]
print(short_names)
upper_long_names = [name.upper() for name in names if len(name) > 4]
print(upper_long_names)

noombers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared = [n * n for n in noombers]
print(squared)

# list_of_strings = input().split(',')
# even_nums = [int(s) for s in list_of_strings if int(s) % 2 == 0]
# print(even_nums)


with open('file1.txt', mode='r') as file:
    f1 = file.readlines()


with open('file2.txt', mode='r') as file:
    f2 = file.readlines()

commons = [int(n) for n in f2 if n in f1]
print(commons)


# student_scores = {student: random.randint(1, 100) for student in names}

# passed_students = {student: score for (
#     student, score) in student_scores.items() if score > 69}
# print(passed_students)

# sentence = input().split()

# sentence_d = {word: len(word) for word in sentence}
# # sentence_d = {word: len(word) for word in sentence.split()} this also works
# print(sentence_d)


weather_c = eval(input())

weather_f = {day: (int(temp) * 9/5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)
