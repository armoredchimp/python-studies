# print("Hello World!")

# print("Hello!\nHello new Line!\nAnd the third.")

# print("Hello" + " Matt")
# print("Hello"+""+"Matt")

# print("Hello" + input("Your name?!"))
# # comment

# name = input("what's your name?")
# print(name)
# name = "Matt"  # replaces previous name
# length = len(name)
# print(length)

# print("Welcome to the Band Name Generator.\nWhat's the name of the city you grew up in?\n")
# city = input()
# print("What's your pet's name?\n")
# pet = input()
# print("Your band name could be " + city + pet)


# Day2
# print("Hello"[4])  # prints o

# print(123 + 345)  # 468, adds them

# 123_456_789  # 123,456,789 or 123456789

# num_char = len(input("Your name?"))
# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters.")

# two_digit_number = input("Type a two digit number: ")
# print(int(two_digit_number[0])+int(two_digit_number[1]))


# height = input('enter height:')
# weight = input('enter weight:')
# bmi = int(weight) / float(height) ** 2
# print(int(bmi))


# print(round(8 / 3, 2))
# print(8 // 3)  # int instead of float as for one /

# # f-string, template literal basically?
# score = 0
# winning = False
# print(f"your score is {score} and you are winning is {winning}")


# tip calculator
# bill = float(input("Total bill: "))
# people = int(input("How many people?"))
# while True:
#     tip = int(input("What percentage do you want to tip?"))
#     if 0 <= tip <= 100:
#         break
#     else:
#         print("Enter a valid percentage number")
# tipN = (bill / 100) * tip

# final = (tipN + bill) / people
# print(
#     f"The total tip is ${tipN:.2f} from a bill of ${bill:.2f}, or ${(tipN + bill):.2f} in total. {people} people will split the total, and each should pay ${final:.2f}.")


# # Day 3

# height = int(input("What is your height?"))
# if height >= 120:
#     print("Tall enough")
#     age = int(input("What is your age?"))
#     if age <= 18:
#         print("You owe $7")
#     elif age >= 8 & age < 18:
#         print("You owe $10")
#     else:
#         print("You owe $43!!!")
# else:
#     print("Too short")
# if height == 120:
#     print("Exactly 120")


# number = int(input("Which number do you want to check? "))

# if (number % 2) != 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")

# BMI 2
# weight = float(input("Weight in kg:"))
# height = float(input("Height in m:"))

# bmi = round(weight / (height ** 2))

# if bmi < 18.5:
#     fatness = "you are underweight."
# elif bmi > 18.5 and bmi <= 25.0:
#     fatness = "you have a normal weight."
# elif bmi > 25.0 and bmi <= 30.0:
#     fatness = "you are slightly overweight."
# elif bmi > 30.0 and bmi <= 35.0:
#     fatness = "you are obese."
# else:
#     fatness = "you are clinically obese."
# print(f"Your BMI is {bmi}, {fatness}")


# Leap Year
# year = int(input("Enter year:"))
# leap = False
# if year % 4 == 0:
#     leap = True
#     if year % 100 == 0:
#         leap = False
#         if year % 400 == 0:
#             leap = True

# if leap == True:
#     print("Leap year.")
# else:
#     print("Not leap year.")


# Pizza Order
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# if add_pepperoni == "Y":
#     if (size == "M" or size == "L"):
#         bill += 3
#     else:
#         bill += 2
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")


# Love calculator
# name1 = input("First name:")
# name2 = input("Second name:")


# combined = name1 + name2
# combined = combined.lower()

# counter1 = 0
# counter2 = 0
# counter1 += combined.count('t')
# counter1 += combined.count('r')
# counter1 += combined.count('u')
# counter1 += combined.count('e')
# counter2 += combined.count('l')
# counter2 += combined.count('o')
# counter2 += combined.count('v')
# counter2 += combined.count('e')


# combinedN = int(str(counter1) + str(counter2))


# if combinedN < 10 or combinedN > 90:
#     print(f"Your score is {combinedN}, you go together like coke and mentos.")
# elif combinedN >= 40 and combinedN <= 50:
#     print(f"Your score is {combinedN}, you are alright together.")
# else:
#     print(f"Your score is {combinedN}.")

# Treasure Island, obviously this is spaghetti code but that's the point of the exercise
# lr = input("Welcome to Treasure Island. On the left, you see a beach filled with rowdy pirates. On the right, you see a path leading into the jungle. Go left or go right?").lower()
# if lr == "left":
#     print("The pirates quickly see you as an easy mark, you are robbed and beaten to within an inch of your life. They leave you for dead. Game Over!")
#     exit
# elif lr == "right":
#     swim = input("The path soon leads to a raging river. Behind you, you hear the clamor of the pirates from the beach who noticed you and are now in pursuit. The river looks like it could be too dangerous, but upstream you notice a raft of sorts, barreling towards you. You could probably jump on it and then make your way across, but that would require waiting for another minute or two. Wait for the raft or try and swim?").lower()

#     if swim == "wait" or swim == "raft":
#         print("The pirates arrive sooner than expected and shoot you in the leg. You are enslaved. Game Over!!")
#         exit
#     elif swim == "swim":
#         print("Although it is a struggle, you manage to barely swim across the river, bruising yourself in the process but arriving in once piece.")
#         print("The path leads deep into the jungle. After some time, you come upon a small temple containing three doors. The first door has a dancing maiden on it, the middle door depicts a skull, and the final door shows a groveling beggar.")
#         door = input("Which door do you choose? Left, middle, or right?")
#         door = door.lower()
#         if door == "left":
#             print("A beautiful woman sits on a divan. She beckons you closer. Entranced, you approach, only to be instantly killed as she reveals herself to be a demon. Your last moment is seeing her face transform into an sharp-toothed horror with glowing green eyes. You Lose!!")
#             exit
#         elif door == "middle":
#             print("You are instantly killed by the necromantic curse that fills this room. The door had a skull on it, was that really the one you picked? Try Again!!")
#             exit
#         elif door == "right":
#             print("Inside is a wise shaman who congratulates you on picking the correct door. He grants you infinite magical powers and the ability to speak time and bend space. You Win!!")
# else:
#     print("You failed to go in either direction. The pirates from the beach soon notice you and you are enslaved. Game Over!")
#     exit

import math
import random
import py_module

# random_int = random.randint(1, 10)
# print(random_int)
# print(py_module.specialnumber)

# random_float = random.random()
# print(random_float)
# random_float * 100  # random number 0-99.99999

# coin_flip = random.randint(1, 2)
# if coin_flip == 1:
#     print("Heads")
# else:
#     print("Tails")


# list = ["a", "b", "c"]
# list[2] = "d"
# print(list)  # a, b, d

# list.append("e")
# list.extend(["f", "g"])
# print(list)


# Banker Roulette
# str = input("Type a list of names seperated by commas:\n")
# strSpl = str.split(",")
# print(strSpl[random.randint(0, len(strSpl) - 1)])

# # OR
# print(random.choice(strSpl))

# Treasure Map - this one kicked my ass :(
# row1 = ["", "️", "️"]
# row2 = ["", "", "️"]
# row3 = ["", "", ""]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# res = [int(position[0]), int(position[1])]
# print(res)


# map[res[0] - 1][res[1] - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

# Rock Paper Scissors - didn't follow instructions correctly, we were supposed to take 0, 1, or 2 as inputs but this works
# Rock = "Rock"
# Paper = "Paper"
# Scissors = "Scissors"
# RPS = [Rock, Paper, Scissors]

# player = input("Pick rock, paper, or scissors:\n").lower()
# computer = RPS[random.randint(0, 2) - 1]


# def tie():
#     print("Tie game")


# def loss():
#     print("You Lose!")


# def win():
#     print("You Win!")


# if player == "rock":
#     if computer == Rock:
#         tie()
#     elif computer == Paper:
#         loss()
#     elif computer == Scissors:
#         win()
# elif player == "paper":
#     if computer == Rock:
#         win()
#     elif computer == Paper:
#         tie()
#     elif computer == Scissors:
#         loss()
# elif player == "scissors":
#     if computer == Rock:
#         loss()
#     elif computer == Paper:
#         win()
#     elif computer == Scissors:
#         tie()
# else:
#     print("Invalid input")

# RPS = ["rock", "paper", "scissors"]
# player = input("Pick rock, paper, or scissors:\n").lower()
# computer = random.choice(RPS)
# if player == computer:
#     print("Tie game")
#     print(f"You and the computer both picked {player.capitalize()}")
# elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
#     print("You win!")
#     print(
#         f"You picked {player.capitalize()}, and the computer foolishly picked {computer.capitalize()}!")
# elif (player == "rock" and computer == "paper") or (player == "scissors" and computer == "rock") or (player == "paper" and computer == "scissors"):
#     print("You Lose!")
#     print(
#         f"You mistakenly picked {player.capitalize()} and the computer picked {computer.capitalize()}.")
# else:
#     print("Invalid input")

#  # GPT made this one, I did 0 of it but leaving it here for reference:


# def rock_paper_scissors():
#     RPS = ["rock", "paper", "scissors"]

#     game_rules = {
#         "rock": "scissors",
#         "scissors": "paper",
#         "paper": "rock"
#     }

#     player = input("Pick rock, paper, or scissors:\n").lower()
#     computer = random.choice(RPS)

#     if player == computer:
#         print("Tie game")
#         print(f"You and the computer both picked {player.capitalize()}")
#     elif game_rules[player] == computer:  # Player's choice defeats computer's choice
#         print("You win!")
#         print(
#             f"You picked {player.capitalize()}, and the computer foolishly picked {computer.capitalize()}!")
#     elif player in RPS:  # Computer's choice defeats player's choice
#         print("You Lose!")
#         print(
#             f"You mistakenly picked {player.capitalize()} and the computer picked {computer.capitalize()}.")
#     else:
#         print("Invalid input")


# rock_paper_scissors()


# Day 5
# nums = ["1", "2", "3"]
# for num in nums:
#     print(num)
#     print(num + "A")
# print(nums)

# Height calculator. Stupid exercise that actively teaches bad progamming habits
# student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total = 0
# count = 0
# for height in student_heights:
#     total += height
#     count += 1
# print(round(total / count))

# student_heights = input("Input a list of student heights ").split()
# total = 0
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     total += student_heights[n]
# print(round(total / len(student_heights)))

# student_heights = input("Input a list of student heights ").split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# print(round(sum(student_heights) / len(student_heights)))


# Highest Score
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# highest = 0
# for score in student_scores:
#     if (score > highest):
#         highest = score
# print(f"The highest score in the class is: {highest}")

# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number

# final = 0
# for number in range(0, 101, 2):
#     final += number
#     print(number)
# print(final)

# FizzBuzz
# for number in range(1, 100):
#     if ((number % 3 == 0) and (number % 5 == 0)):
#         print("FizzBuzz")
#     elif (number % 5 == 0):
#         print("Buzz")
#     elif (number % 3 == 0):
#         print("Fizz")
#     else:
#         print(number)

# Password generator - did this before I knew there was a shuffle(), that would have been helpfuL!
import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# password = []
# # final = []
# for number in range(0, nr_letters):
#     password.append(random.choice(letters))
# for number in range(0, nr_symbols):
#     password.append(random.choice(symbols))
# for number in range(0, nr_numbers):
#     password.append(random.choice(numbers))
# # for number in range(0, len(password)):
# #     char = random.choice(password)
# #     password.remove(char)
# #     final.append(char)

# random.shuffle(password)
# password = ''.join(password)
# print(password)

# # Day 6


# def my_function():
#     print("Hello")


# Hangman
# stages = ['''

#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========

# ''', '''

#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========

# ''', '''

#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========

# ''', '''

#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''

#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========

# ''', '''

#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========

# ''', '''

#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========

# ''']
# word_list = ["penguin", "monkey", "castle", "palace"]
# random_word = random.choice(word_list)
# revealed_word = []
# guesses = 6

# for letter in random_word:
#     revealed_word.append("_")

# for char in revealed_word:
#     print(f"{char} ", end="")

# while guesses > 0:
#     count = 0
#     guess = input("\nGuess a letter:").lower()
#     correct_guess = False
#     for letter in random_word:
#         if guess == letter:
#             print(f"{letter} ", end="")
#             count += 1
#             revealed_word[count - 1] = guess
#             correct_guess = True
#         else:
#             count += 1
#             print(f"{revealed_word[count - 1]} ", end="")
#     if correct_guess == False:
#         guesses -= 1
#         print(stages[guesses])
#     if guesses == 0:
#         if list(random_word) == revealed_word:
#             print("\nVictory!")
#             exit()
#         else:
#             print("\nDefeat!")
#             exit()
#     if list(random_word) == revealed_word:
#         print("\nVictory!")
#         exit()


# Day 8

# def greet(name):

#     print(f"Hello {name}")


# greet("Peter")


# def salute(name, rank):
#     print(f"A salute to {rank} {name.upper()}!")


# salute("Johnston", "Corporal")
# salute(rank="Sergeant", name="Coward")


# # Paint wall
# def paint_calc(height, width, cover):
#     print(
#         f"You'll need {(math.ceil((int(height)*int(width)) / cover))} cans of paint.")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime number detector
# n = int(input("Check this number: "))


# def prime_checker(number):
#     prime = False
#     if number <= 1:
#         print("It's not a prime number")
#         exit()
#     elif number == 2 or number == 3:
#         print("It's a prime number")
#         exit()
#     for num in range(2, math.ceil(math.sqrt(number))):
#         if number % num == 0:
#             prime = False
#             print("It's not a prime number")
#             break
#         else:
#             prime = True
#     if prime == True:
#         print("It's a prime number")


# prime_checker(number=n)

# Caesar Cipher
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def init():
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     if direction.lower() == 'encode':
#         code(text, shift, True)
#     elif direction.lower() == 'decode':
#         code(text, shift, False)
#     else:
#         print("Enter encode or decode")
#         init()


# def code(text, shift, bool):
#     cipher = []
#     if bool == False:
#         shift *= -1
#     for letter in text:
#         if letter not in alphabet:
#             cipher.append(letter)
#         else:
#             cipher.append(alphabet[((alphabet.index(letter)) + shift) % 26])

#     print(''.join(cipher))
#     again = input("Another one?").lower()
#     if again == 'yes' or again == 'ok' or again == 'absolutely':
#         init()
#     else:
#         exit()


# init()


# I modified some dude's code on Udemy to add the repeating functionality as a challenge:
# def encrypted(text, shift):
#     encrypted_message = []
#     for letter in text:
#         # find the index of the letter in the alphabet list
#         new_index_num = (alphabet.index(letter)+shift) % 26
#         new_index = alphabet[new_index_num]
#         encrypted_message.append(new_index)

#     new_message = "".join(encrypted_message)
#     print(f"Cipher Text: {new_message}")
#     print(f"The encoded text is {new_message} ")
#     again()


# def decode(text, shift):
#     decode_message = []
#     for letter in text:
#         # find the index of the letter in the alphabet list
#         new_index_num = (alphabet.index(letter)-shift) % 26
#         new_index = alphabet[new_index_num]
#         decode_message.append(new_index)

#     new_message = "".join(decode_message)
#     print(f"The Text: {new_message}")
#     print(f"The  decoded text is {new_message} ")
#     again()


# def again():
#     again_response = input("Repeat?yes/no:").lower()
#     if again_response == 'yes':
#         caesar()
#     else:
#         exit()


# def caesar():
#     direction = input(
#         " type ' encode ' to encrypt, type 'decode' to decrypt: \n ")
#     text = input("type your message: ").lower()
#     shift = int(input("type the shift number: "))

#     if direction == "encode":
#         encrypted(text, shift)
#     elif direction == "decode":
#         decode(text, shift)
#     else:
#         print(" Invalid choice. ")
#         caesar()
# caesar()


# Day 9
# dict = {
#     "one": "part one",
#     "two": "part two",
# }

# dict["three"] = "part three"  # part three kvp added

# for key in dict:
#     print(dict[key])  # just prints all three values only

# dict = {}  # is now empty


# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}
# for key, value in student_scores.items():
#     if value <= 100 and value >= 91:
#         value = "Outstanding"
#     elif value <= 90 and value >= 81:
#         value = "Exceeds Expectations"
#     elif value <= 80 and value >= 71:
#         value = "Acceptable"
#     else:
#         value = "Fail"

#     student_grades[key] = value


# print(student_grades)


# countries = {
#     "France": {"cities_visited": ["Paris", "Marseille", "Lyon", "Dijon"],
#                "Language": "French"
#                },
#     "China": ["Beijing", "Shanghai", "Wuhan"]
# }

# big_list = [
#     {"country": "France", "cities_visited": ["Paris", "Marseille", "Lyon", "Dijon"],
#      "Language": "French"},
#     {"country": "Belgium", "cities_visited": ["Brussels", "Bruge"],
#      "Language": "French"},
# ]

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]


# def add_new_country(country, times, cities):
#     arr = []
#     for city in cities:
#         arr.append(city)

#     travel_log.append({"country": country, "visits": times, "cities": arr})


# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# Secret Auction
# guests = int(input("How many secret bidders?\n"))
# auction = {}
# for guest in range(0, guests):
#     name = input("Your name?\n")
#     bid = int(input("Your maximum bid?\n"))

#     auction[name] = bid
# highest = 0
# bidder = ''


# def bid_calculation(object, number, name):
#     for key, value in object.items():
#         if value > number:
#             number = value
#             name = key
#     print(f"{name} secures the contract with a bid of ${number}.")


# bid_calculation(auction, highest, bidder)


# def format_name(fName, lName):
#     a = fName.title()
#     b = lName.title()
#     return a, b


# def is_leap(year):

#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# def days_in_month(year, month):
#     leapV = is_leap(year)
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if leapV == True:
#         month_days[1] = 29
#     return month_days[month - 1]


# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Calc
# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 * n2


# def divide(n1, n2):
#     return n1 / n2


# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# num1 = float(input("What's the first number?"))
# for symbols in operations.keys():
#     print(symbols)
# operation = input("Pick a math operation: \n")
# num2 = float(input("What's the second number?"))


# calc = operations[operation]
# answer = calc(num1, num2)

# print(f"{num1} {operation} {num2} = {answer}")
# # lazy garbage below, I didn't feel like re-factoring and doing it correctly =\. Last lesson of the night
# calculating = True
# while calculating == True:
#     again = input("Keep going? y or n:\n").lower()
#     if again == "y":
#         next_num = int(input("What's the next number?"))
#         for symbols in operations.keys():
#             print(symbols)
#         operation = input("Pick a math operation: \n")
#         calc = operations[operation]
#         next_answer = calc(answer, next_num)
#         print(f"{answer} {operation} {next_num} = {next_answer}")
#         answer = next_answer
#     else:
#         calculating = False

# Blackjack

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# def validate(player_cards, comp_cards):
#     if (sum(player_cards)) > 21:
#         if 11 in player_cards:
#             player_cards[player_cards.index(11)] = 1
#             return validate(player_cards, comp_cards)
#         print(f"Bust, you had {sum(player_cards)}")
#         exit()
#     elif (sum(comp_cards)) > 21:
#         if 11 in comp_cards:
#             comp_cards[comp_cards.index(11)] = 1
#             return validate(player_cards, comp_cards)
#         print(f"You win with {sum(player_cards)} over {sum(comp_cards)}")
#         exit()
#     elif (sum(player_cards) == 21 and (sum(comp_cards)) == 21):
#         print(f"Draw, both had 21")
#         exit()
#     elif (sum(player_cards) == 21):
#         print("Blacjack, you win!")
#         exit()
#     elif (sum(comp_cards) == 21):
#         print("Dealer Blackjack, you lose")
#         exit()
#     else:
#         return


# def contin(player_cards, comp_cards):
#     cont = input("Type 'y' to get another card, type 'n' to pass:")
#     if cont == 'y':
#         player_cards.append(random.choice(cards))
#         validate(player_cards, comp_cards)
#         print(
#             f"Your cards: {player_cards}, current score: {sum(player_cards)}")
#         contin(player_cards, comp_cards)
#     elif cont == 'n':
#         computer(player_cards, comp_cards)


# def computer(player_cards, comp_cards):
#     comp_cards.append(random.choice(cards))
#     validate(player_cards, comp_cards)
#     if 21 - (sum(comp_cards)) <= 2:
#         compare(player_cards, comp_cards)
#     elif (21 - (sum(comp_cards))) > 2 and (21 - (sum(comp_cards))) <= 7:
#         l = [0, 1]
#         if (random.choice(l)) == 1:
#             computer(player_cards, comp_cards)
#         else:
#             compare(player_cards, comp_cards)
#     else:
#         computer(player_cards, comp_cards)


# def compare(player_cards, comp_cards):
#     if sum(player_cards) == sum(comp_cards):
#         print(f"Draw, both had {sum(player_cards)}")
#         exit()
#     elif sum(player_cards) > sum(comp_cards):
#         print(
#             f"You won! You had {sum(player_cards)} and the dealer had {sum(comp_cards)}")
#         exit()
#     else:
#         print(
#             f"Dealer won with {sum(comp_cards)} over your {sum(player_cards)}")
#         exit()


# player_cards = random.sample(cards, 2)
# comp_cards = [random.choice(cards)]
# print(player_cards, comp_cards)
# print(
#     f"Your cards: {player_cards}, current score: {player_cards[0] + player_cards[1]}\nComputer's first card: {comp_cards[0]}")
# comp_cards.append(random.choice(cards))
# validate(player_cards, comp_cards)
# contin(player_cards, comp_cards)


# Number Guessing Game


def init():
    print("Welcome to Number Guess!\nI'm thinking of a number between 1 and 100.")

    def diff():
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

        if difficulty == 'easy':
            attempts = 10
            secret_number = random.randint(1, 100)
            guess(attempts, secret_number)
        elif difficulty == 'hard':
            attempts = 5
            secret_number = random.randint(1, 100)
            guess(attempts, secret_number)
        else:
            print("Enter a valid input")
            diff()
    diff()


def wrong(attempts, secret_number):
    attempts -= 1
    if attempts == 0:
        print("You lose!")
        again = input("Play again? Type 'y':")
        if again == 'y':
            init()
        else:
            exit()
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess(attempts, secret_number)


def guess(attempts, secret_number):
    player_guess = int(input("Make a guess: "))
    if (player_guess < secret_number):
        print("Too low.\nGuess again.")
        wrong(attempts, secret_number)
    elif (player_guess > secret_number):
        print("Too high.\nGuess again.")
        wrong(attempts, secret_number)
    elif (player_guess == secret_number):
        print(f"Correct! You win! {player_guess} was the number.")
        exit()
    else:
        print("Enter a valid input")
        guess(attempts, secret_number)


init()
