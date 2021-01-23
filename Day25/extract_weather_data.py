

# data = []
# with open("weather_data.csv", "r") as data_file:
#     weather_data = data_file.readlines()
#     for line in weather_data:
#         line = line.replace("\n", " ")
#         line = line.strip()#
#         data.append(line)
#
# print(data)

# import csv
# from typing import List
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # for row in data:
#     #     print(row)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data.temp

# print(temp_list)
#
# mean_temp = temp_list.mean()
# print(mean_temp)
#
#
# #Get Data in Columns
# print(data.condition)
# print(data["condition"])

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(monday_temp * 9/5 + 32, "F")