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
bill = float(input("Total bill: "))
people = int(input("How many people?"))
while True:
    tip = int(input("What percentage do you want to tip?"))
    if 0 <= tip <= 100:
        break
    else:
        print("Enter a valid percentage number")
tipN = (bill / 100) * tip

final = (tipN + bill) / people
print(
    f"The total tip is ${tipN:.2f} from a bill of ${bill:.2f}, or ${(tipN + bill):.2f} in total. {people} people will split the total, and each should pay ${final:.2f}.")
