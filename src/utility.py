from bs4 import BeautifulSoup
class Utility():

	@staticmethod
	def preprocessFilename(url):
		idx = url.find('://')
		filename = url[idx+3:]
		idx = filename.find('www.')
		if idx >=0 :
			filename = filename[4:]

		filename = filename.replace('/', '.')
		return filename



	@staticmethod
	def findUrls(page):
		soup = BeautifulSoup(page.text, "html.parser")
		return soup.find_all("a", href=lambda href: href and not href.startswith("#"))

	@staticmethod
	def findImages(page):
		soup = BeautifulSoup(page.content, "html.parser")
		return soup.find_all('img')