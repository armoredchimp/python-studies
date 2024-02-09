# try:
#     file = open('nonexistent.txt')
# except FileNotFoundError:
#     print('File not found. Creating new file')
#     file = open('a_file.txt', 'w')
#     file.write('Text here')
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist')
# else:
#     print('File located!')
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is a custom error")
# file.close()
# print('Final process executed. I am done now.')


# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Height should be 3 meters or less")

# bmi = weight / height ** 2
# print(bmi)

# fruits = eval(input())


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + 'pie')
#     except IndexError:
#         print('Fruit Pie')


# make_pie(4)


posts = eval(input())

total_likes = 0

for post in posts:
    try:
        total_likes += post['Likes']
    except KeyError:
        pass

print(total_likes)
