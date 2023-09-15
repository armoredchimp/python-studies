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
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
if add_pepperoni == "Y":
    if (size == "M" or size == "L"):
        bill += 3
    else:
        bill += 2
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
