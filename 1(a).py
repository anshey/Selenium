import requests

url = "https://dummyapi.io/data/v1/user?limit=10"
headers = {
  'app-id': '617f7cf7df767f1aef44ea9c'
}
response = requests.request("GET", url, headers=headers)
response
