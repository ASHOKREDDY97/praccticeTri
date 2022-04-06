# #Make a request to a web page, and print the response text:

# import requests
# x= requests.get('https://w3schools.com/python/demopage.html')
# print(x.text)

# #Make a DELETE request to a web page, and return the response text:

# import requests
# x = requests.delete('https://w3schools.com/python/demopage.html')
# print(x.text)

# ###
# import requests
# url = 'https://w3schools.com/python/demopage.php'
# #Sometimes the server redirects a request, could be if the file does not exist etc., set the 'allow_redirects' parameter to False to deny redirects:
# x = requests.delete(url, allow_redirects=False)
# print(x.text)


# ###
# import requests
# url = 'https://w3schools.com/python/demopage.php'
# #use the 'auth' parameter to send requests with HTTP Basic Auth:
# x = requests.delete(url, auth = ('user', 'pass'))
# print(x.status_code)

# # ###
# import requests
# url = 'https://w3schools.com/python/demopage2.php'
# #use the 'cookies' parameter to send cookies to the server:
# x = requests.delete(url, cookies = {"favcolor": "Red"})
# print(x.status_code)

# ###
# import requests
# url = 'https://w3schools.com/python/demopage.asp'
# #use the 'headers' parameter to set the HTTP headers:
# x = requests.delete(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
# print(x.status_code)

# # Make a HEAD request to a web page, and return the HTTP headers:

# import requests
# x = requests.head('https://www.w3schools.com/python/demopage.php')
# print(x.headers)

# # Make a POST request to a web page, and return the response text:

# import requests
# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}
# x = requests.post(url, data = myobj)
# print(x.text)


# get method
import requests
r = requests.get('https://api.github.com/')
print(r.text)
print(r.status_code)


# params
import requests
payload = {'key1':'value1'}
response=requests.get('https://api.github.com/',params=payload)
print(response.url)
print(response.status_code)


# allow_redirects
import requests
url = 'http://w3schools.com/python/demopage.html'
x = requests.get(url)
print(x.text)
x = requests.get(url, allow_redirects=False)
print(x.text)

# basic auth
import requests
url = 'https://w3schools.com/python/demopage.php'
x = requests.get(url, auth = ('user', 'ashok'))
print(x.status_code)


# headers
import requests
url = 'https://w3schools.com/python/demopage.asp'
x = requests.get(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
print(x.text)

# cookies
import requests
url = 'https://w3schools.com/python/demopage2.php'
x = requests.get(url, cookies = {"favcolor": "Red"})
print(x.text)


# # post method
import requests
payload = {'key1':'value1'}
response=requests.get('https://api.github.com/',data=payload)
print(response.status_code)
print(response.headers)

# json 
import requests
payload = {'key1':'value1'}
response=requests.get('https://api.github.com/',json=payload)
print(response.status_code)

# put
import requests
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
print(r.status_code)
 
 # delete 
r = requests.delete('https://httpbin.org/delete')
print(r.status_code)