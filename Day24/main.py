# with open("file.txt") as file:
#   contents = file.read()
#   print(contents)

with open('file.txt', mode='w') as file:  # mode='a' to append, w writes over
    file.write('New text')


with open('new_file.txt', mode='w') as file:  # mode='a' to append, w writes over
    file.write('Hello, new text here')
