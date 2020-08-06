import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name":"Anoo", "views":1000},
         {"likes": 70, "name":"Visu", "views":50000},
         {"likes": 100, "name":"Hello world API", "views":1300}]

for i in range(len(data)):
    response = requests.put(BASE+"video/"+ str(i), data[i])
    print(response.json())

# response = requests.delete(BASE+"video/2")
# print(response)
# input()
# response = requests.delete(BASE+"video/6")
# print(response)
response = requests.get(BASE+"video/2")
print(response.json())
response = requests.patch(BASE+"video/2",{"views":999})
print(response.json())
