import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
print(fur_color)
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
color_count_dict = {"Squirrels Colors": ["Gray", "Cinnamon", "Black"], "Squirrels Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]}
color_count = pandas.DataFrame(color_count_dict)
color_count.to_csv("data.csv")
