# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd

base = "http://www.foxsports.com/nhl/players?season=2017&page="

proxies = {
  'http': 'http://kataria:TT@172.16.114.8:3128',
  'https': 'https://kataria:TT@172.16.114.8:3128',
}

A=[]
B=[]

# for pageq in range(1,123):
# 	page = requests.get(base + str(pageq),proxies=proxies)

# 	print(pageq)
# 	html 	= page.content
# 	soup 	= BeautifulSoup(html,'lxml')
# 	anch	= soup.findAll('a', class_='wisbb_fullPlayer')
	
# 	for ancor in anch:
# 		B.append(ancor["href"])

	
# temp_df = pd.DataFrame({'url' : B})
# temp_df.to_csv('Names.csv', index = False, encoding = 'utf-8')

base2 = "http://www.foxsports.com"
temp_df = pd.read_csv("Names.csv")
enter = pd.read_csv("Names1.csv")
image = []
position = []
team = []

for i in range(len(temp_df)):
	if(enter['Team'][i]=='0' ):
		url_temp = base2 + temp_df["url"][i]
		print(i)
		while(True):
			print("Getting page "+ temp_df["url"][i])
			try:
				page = requests.get(url_temp, proxies=proxies)
			except requests.exceptions.RequestException as e:  # This is the correct syntax
				print(e)
				continue
			break

		html	= page.content
		soup 	= BeautifulSoup(html,'lxml')
		try:
			img		= soup.find('img', class_='wisfb_headshotImage wisfb_bioLargeImg')
			posi 	= soup.find('div',  class_="wisbb_secondaryInfo")
			print(posi)
			if(posi.find('a') is None):
				teams = 0
				enter["Team"][i] = 'Free Agent'
			else:
				teams	= posi.find('a')
				enter["Team"][i] = teams.find(text = True)
			
			posi 	= posi.find('span')
			enter["Position"][i] = posi.find(text = True)
			enter["Image"][i] =  img['src']
		except:
			enter["Position"][i] = 0
			enter["Image"][i] =  0
			enter["Team"][i] = 0

		
		enter.to_csv('Names1.csv', index = False, encoding = 'utf-8')

