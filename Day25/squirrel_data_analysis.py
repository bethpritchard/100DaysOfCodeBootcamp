import pandas as pd
data = pd.read_csv("squirrel_data.csv")

# gray = 0
# cinnamon = 0
# black = 0
#
# for colour in data["Primary Fur Color"]:
#     if colour == "Gray":
#         gray += 1
#     elif colour == "Cinnamon":
#         cinnamon += 1
#     elif colour == "Black":
#         black += 1

grey_count = sum(data["Primary Fur Color"] == "Gray")
red_count = sum(data["Primary Fur Color"] == "Cinnamon")
black_count = sum(data["Primary Fur Color"] == "Black")

data_dict = {
    "Fur Colour": ["Grey", "Red", "Black"],
    "Count" : [grey_count, red_count, black_count]
}


df = pd.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")
