import requests

geturl = "http://127.0.0.1:5000/users"

headers = {
    "Accept": "application/json",
    "User-Agent" : "Python-Requests-Client"
}

response = requests.get(geturl, headers=headers, timeout=10)

print("get status code:",response.status_code)
print(response.json())

geturl2 = "http://127.0.0.1:5000/users/2"
response = requests.get(geturl2)
print("get2 status code:",response.status_code)
print(response.json())

posturl = "http://127.0.0.1:5000/users"
response = requests.post(posturl)

body1 ={
    "id":3,
    "name":"rani",
}

r1 = requests.post(posturl,json=body1)
print("post status code",r1.status_code)
print(r1.json())

puturl = "http://127.0.0.1:5000/users/3"
response3 = requests.put(puturl)
body1 ={
    "id":3,
    "name":"rahul"
}
r2 = requests.put(puturl,json=body1)
print("put status code:",r2.status_code)
print(r2.json())

geturl3 = "http://127.0.0.1:5000/users"
response4 = requests.get(geturl3)
print("get status code:",response4.status_code)
print(response4.json())

patchurl = "http://127.0.0.1:5000/users"
response5 = requests.patch(patchurl)
body4 ={
    "name":"rahul"
}
r5 = requests.put(puturl,json=body1)
print("put status code:",r5.status_code)
print(r5.json())

geturl4 = "http://127.0.0.1:5000"
response6 = requests.get(geturl4)
print("get status code:",response6.status_code)
print(response6.text)