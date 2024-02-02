try:
    file = open('nonexistent.txt')
except FileNotFoundError:
    print('File not found. Creating new file')
    file = open('a_file.txt', 'w')
    file.write('Text here')
except KeyError as error_message:
    print(f'The key {error_message} does not exist')
else:
    print('File located!')
    content = file.read()
    print(content)
finally:
    print('Final process executed. I am done now.')
