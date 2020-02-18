#Use the Request library
import requests
#Set the target webpage
url = 'http://172.17.50.43/creative'
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t *" ,r.status_code)
#This will just get just the headers
h = requests.head(url)
print("Header:")
print("********")
# To print line by line
for x in h.headers:
    print("\t",x,":",h.headers[x])
print("********")
headers = {
    'User-Agent' : 'Iphone 8'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
