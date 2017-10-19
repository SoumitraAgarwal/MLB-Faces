# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd
import shutil
import requests.packages.urllib3
import time
import os
requests.packages.urllib3.disable_warnings()


data = pd.read_csv("Clean.csv")

proxies = {
  'http': 'http://kataria:TT@172.16.114.8:3128',
  'https': 'https://kataria:TT@172.16.114.8:3128',
}


counts = 0
millis = int(round(time.time() * 1000))

for i in range(len(data)):

	if(i%100 == 0 and i):
		rate = 0.1*counts/(int(round(time.time() * 1000)) - millis)
		print("Counts: " + str(counts) + " in " + str(int(round(time.time() * 1000)) - millis) + "ms, rate: " + str(rate) + "pictures/s")
		counts = 0

	url_temp = data["Image"][i]
	try:
		response = requests.get(url_temp, stream=True)
		if response.status_code == 200:
			counts += 1
			if(data["Position"][i] not in os.listdir('Pictures/Position/')):
				os.mkdir('Pictures/Position/' + data["Position"][i])
			with open('Pictures/Position/'+ data["Position"][i] + '/' + str(i) +'.png', 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
			del response

		response = requests.get(url_temp, stream=True)
		if response.status_code == 200:
			counts += 1
			if(data["Team"][i] not in os.listdir('Pictures/Team/')):
				os.mkdir('Pictures/Team/' + data["Team"][i])
			with open('Pictures/Team/'+ data["Team"][i] + '/' + str(i) +'.png', 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)
			del response
	except requests.exceptions.RequestException as e:  # This is the correct syntax
		print(e)