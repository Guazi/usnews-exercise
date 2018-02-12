Author: Daniel Avery
Public Git: https://github.com/Guazi/usnews-exercise
Developed and tested using Python 3.6 on Ubuntu Linux

Introduction:
My name is Daniel Avery.  I love programming specifically in python. 
Thank you for the opportunity to be considered for the Python Developer 
position and for the chance to join your team.  

If you have any comments or questions, please reach out to me by email 
at daniel@danielavery.net or by phone at 202-595-4670

How to install the requirements:
Extract the code to a new directly.  Open the command line and cd to 
that directory.  Type pip install -r requirements.txt 
This will install the requirements (flask, flask-restful, and webargs)

If you prefer to install the requirements line by line, type:
pip install flask flask-restful webargs

How to run the api:
cd to the base directory and type python api.py
This will start the flask server on port 4002

How to test:
Open your web-browser and browse to 
http://localhost:4002/api?word=fizz&max_value=30
Change the word and max_value per the instructions to the values 
you want to test.

You could alternatively use curl to test it:
curl -X GET 'http://localhost:4002/api?word=fizz&max_value=30'

Expected Response:
{"status":"ok","numbers":[3,6,9,12,15,18,21,24,27,30]}

How I built this:

I built on the boilerplate code provided by the webargs framework, 
which can be found here:

https://github.com/sloria/webargs/blob/dev/examples/flaskrestful_example.py

I also have an API endpoint set up for my React App that uses flask at 
http://52.179.0.193:5000/item?upc= 
that I based my work on. A valid UPC will return a JSON response of the 
item data from MongoDB using pymongo 
(example: http://52.179.0.193:5000/item?upc=041800716005)