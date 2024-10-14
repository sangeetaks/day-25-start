# with open("weather_data.csv","r") as file:
#     data = file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
# print(temperature)
import pandas

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# temp_avg = sum(temp_list)/len(temp_list)
# print(temp_avg)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
#
# monday =data[data.day=="Monday"]
# print(monday.condition)
# temp_in_f = monday.temp*(9/5) + 32
# print(temp_in_f)


# data_dict =data.to_dict()
# print(data_dict)


# data_dict ={
#     "students": ["Amy","James","Angela"],
#     "scores":[76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241013.csv")
my_list = data["Primary Fur Color"].value_counts()
df = pandas.DataFrame(my_list)
df.to_csv("squirrel.count.csv")

