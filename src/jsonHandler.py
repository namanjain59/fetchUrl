from datetime import datetime
import json

class JsonHandler():

	def writeJson(self, urls, images, filename):
		data = {}
		data['site'] = filename
		data['num_links'] = urls
		data['images'] = images
		date =  datetime.utcnow()
		last_time = date.strftime("%a %b %d %Y, %H:%M:%S UTC") 
		data['time'] = last_time

		with open(filename+'.txt', 'w') as outfile:
			json.dump(data, outfile)
		print(filename +" fetched successfuly")


	def readJson(self, filename):
		try :
			with open(filename+'.txt') as json_file:
				data = json.load(json_file)
				print('site: ' , data['site'])
				print('num_links: ' , data['num_links'])
				print('images: ' , data['images'])
				print('last_fetch: ' , data['time'])
				print(' ')
		except Exception as err:
				print (filename, " has not been fetched yet, Fetch it first!")