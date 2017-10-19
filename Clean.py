import pandas as pd

data = pd.read_csv("Names1.csv")

data = data[data["Image"] != "#"]
data = data.reset_index()
images = []
for i in range(len(data)):
	temp = data["Image"][i].split(".")
	temp[4] = '700'
	temp[5] = '850'

	temp = '.'.join(temp)
	print(data["url"][i])
	images.append(temp)
data["Image"] = images
data.to_csv("Clean.csv", index = False)