import csv
import pandas as pd

# with open('weather_data.csv', 'r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         print(row)
#         temperatures.append(int(row[1]))
#     temperatures.pop(0)
#     print(temperatures)

# data = pd.read_csv('weather_data.csv')
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)


def average_from_list(list):
    print(sum(list) / len(list))


# average_from_list(temp_list)

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.temp)  # why didn't she just show us this way first >:(

# # Get data in row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.temp * (9/5) + 32)  # valid


# data2 = pd.DataFrame(data_dict)
# data2.to_csv('new_data.csv')


# squirrel_data = pd.read_csv('squirrel_data.csv')
# furs = squirrel_data['Primary Fur Color']
# fur_values = furs.value_counts()
# fur_values.to_csv('fur.csv')


# More efficient but less readable version:
# fur_values = pd.read_csv('squirrel_data.csv')['Primary Fur Color'].value_counts()
# fur_values.to_csv('fur.csv')
