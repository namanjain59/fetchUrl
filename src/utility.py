import requests
from collections import Counter
from bs4 import BeautifulSoup
import json
from datetime import datetime


class Utility():

	@staticmethod
	def readJson(filename):
		with open(filename+'.txt') as json_file:
			data = json.load(json_file)
			print('site: ' , data['site'])
			print('num_links: ' , data['num_links'])
			print('images: ' , data['images'])
			print('last_fetch: ' , data['time'])
			print(' ')

	@staticmethod
	def fetchMetaData(urlList):
		for url in urlList:
			try :
				page = requests.get(url)
				idx = url.find('://')

				filename = url[idx+3:]

				Utility.readJson(filename)
			except Exception as err:
				print (str(err))


	@staticmethod
	def storeJson(urls, images, filename):
		data = {}
		data['site'] = filename
		data['num_links'] = urls
		data['images'] = images
		date =  datetime.utcnow()
		last_time = date.strftime("%a %b %d %Y, %H:%M:%S UTC") 
		data['time'] = last_time
		#print(last_time)
		with open(filename+'.txt', 'w') as outfile:
			json.dump(data, outfile)
		print(filename +" fetched successfuly")


	@staticmethod
	def storeMetaData(page, filename):
		soup = BeautifulSoup(page.text, "html.parser")
		foundUrls = soup.find_all("a", href=lambda href: href and not href.startswith("#"))
		#print (foundUrls)
		#print (len(foundUrls))

		soup = BeautifulSoup(page.content, "html.parser")
		foundImages = soup.find_all('img')
		#print(foundImages)
		#print(len(foundImages))
		Utility.storeJson(len(foundUrls), len(foundImages), filename)

	@staticmethod
	def fetchWebPages (urlList):
		for url in urlList:
			try :
				page = requests.get(url)
				idx = url.find('://')

				filename = url[idx+3:]
				#print (filename)
				page_content = page.text
				with open(filename+ '.html', 'w', encoding='utf8') as fp:
					fp.write(page_content)

				Utility.storeMetaData(page, filename)
			except Exception as err:
				print (str(err))


