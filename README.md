# fetchUrl!

Fetch webpages with the given urls


## Steps (using python 3)

1) Create a python virtual env and activate it
2) run requirements.txt file

	    pip install -r requirements.txt
    
3. Run the fetch.py file!
	a) To fetch Urls
	

	    python src\fetchUrl.py https://google.com https://gmail.com

	b) To get metadata:
		
	    python src\fetchUrl.py --metadata https://google.com https://gmail.com
	    

## Steps (using docker)

1) Build docker file

	    docker build -t fetch .
2) Run the fetch image!
	a) To fetch Urls
	

	    docker run --rm fetch https://google.com https://gmail.com

	b) To get metadata:
		
	    docker run --rm fetch --metadata https://google.com https://gmail.com

**Note:** Data is getting stored in docker container in this case. I'm yet to figure out how to get that data into local storage
