import requests

url="https://v2.jokeapi.dev/joke/Any?format=json"
json_data=requests.get(url).json()


arr=["",""]
arr[0]=json_data["setup"]
arr[1]=json_data["delivery"]

def joke1():
    return arr

# pr=joke1()
# print(pr)