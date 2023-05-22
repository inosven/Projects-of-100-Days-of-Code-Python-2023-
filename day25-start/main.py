# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#             print(row)
# print(temperatures)
import numpy
import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# # data_dict = data.to_dict()
# # print(data_dict)
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # mean_temp = data["temp"].mean()
# # # print(mean_temp)
# # print(data["temp"].max())
# ## Get Data in Column
# # print(data["condition"])
# # print(data.condition)
#
# ## Get data in row
#
# # print(data[data["temp"] == data["temp"].max()])
#
# # monday = data[data.day == "Monday"]
# # # print(monday.condition)
# # print(monday.temp * 9 / 5 + 32)
#
# ## Create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"], "score": [76, 75, 65]
# }
# data_frame = pd.DataFrame(data_dict)
# print(data_frame)
# data_frame.to_csv("new_data_file")
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.head(5))
gray_number = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_number)
red_number = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_number = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[gray_number, red_number, black_number]
}
pd.DataFrame(data_dict).to_csv("squirrel_count.csv")
