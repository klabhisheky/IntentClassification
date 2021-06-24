Make sure packages from requirement.txt are installed properly use the below command
	pip install -r requirement.txt
Code is written with python3.7, running on this version is highly recemmended
After installing all the packages install nltk stopwords with below command
   	python -m nltk.downloader stopwords
Using virtualenv is highly recemmended

Change the Server address to the LOCATION and PORT you choose to run server on from "js/constant.js"

Currently Server address is set to deployed version of server over pythonanywhere.com, Please use that for running code (untill local configuration is properly set)


Steps to RUN:
1. run server.py from cmd ( >python server.py)
2. run index.html (with correct set of serveraddress and ports -> it could be located in cmd after running server)
