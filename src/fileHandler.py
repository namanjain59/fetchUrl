class FileHandler():
	
	def writeData(self, filename, data):
		with open(filename, 'w', encoding='utf8') as fp:
			fp.write(data)
