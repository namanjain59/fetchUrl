import getopt, sys
from webInterface import WebInterface
import os
 
argumentList = sys.argv[1:]
 
long_options = ["metadata"]
 
filestart = 1
option = 1
try:
    arguments, values = getopt.getopt(argumentList, [], long_options)
    
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-m", "--metadata"):
            filestart = 2
            option = 2
        break     
except getopt.error as err:
    print (str(err))

urlList = sys.argv[filestart:]
#print(urlList)
webInterface = WebInterface()

if option == 1:
	webInterface.fetchWebPages(urlList)
else :
	webInterface.fetchMetaData(urlList)