##
import requests
response = requests.get('https://api.github.com')
if response.status_code ==200:
    print('success')
else:
    print('not found')
##

##
import requests
response = requests.get('https://api.github.com')
if response.status_code==200:
    print('success')
elif response.status_code == 404:
    print('Not Found')
##


##
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!')
##

##
import requests
x = requests.get('https://w3schools.com/python/demopage.html')
print(x.text)
##


Make a DELETE request to a web page, and return the response text:
import requests
x = requests.delete('https://w3schools.com/python/demopage.php')
print(x.text)


Get Status code
import requests
x = requests.get('https://w3schools.com')
print(x.status_code)

params
import requests
url = 'https://w3schools.com/python/demopage.php'
#demonstrate how to use the 'params' parameter:
response = requests.get(url, params = {"model": "Mustang"})
#print the response (the content of the requested file):
print(response.text)
#the file 'demopage.php' looks for a 'model' query string and prints its value.


# Auth
import requests

url = 'https://w3schools.com/python/demopage.php'

#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.get(url, auth = ('user', 'pass'))

print(x.status_code)
