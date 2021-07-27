import requests
from jsonHandler import JsonHandler
from fileHandler import FileHandler
from utility import Utility

class WebInterface():
	def __init__(self):
		self.jsonHandler = JsonHandler()
		self.fileHandler = FileHandler()

	def fetchMetaData(self, urlList):
		for url in urlList:
			try :
				page = requests.get(url)
				filename = Utility.preprocessFilename(url)
				self.jsonHandler.readJson(filename)

			except Exception as err:
				print (str(err))
	
	def fetchWebPages (self, urlList):
		for url in urlList:
			try :
				page = requests.get(url)
				filename = Utility.preprocessFilename(url)
				self.storeMetaData(page, filename)
				self.fileHandler.writeData(filename+".html", page.text)
			except Exception as err:
				print (str(err))


	def storeMetaData(self, page, filename):
		foundUrls = Utility.findUrls(page)
		foundImages = Utility.findImages(page)
		#Can add more data here if required

		self.jsonHandler.writeJson(len(foundUrls), len(foundImages), filename)



