import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth


username = input("Please enter username: ")
password = getpass("Please enter password: ")

url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

url2 = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

Token = requests.request("POST", url, headers=headers, data=payload)

payload2={}
headers2 = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2MTIzZGEzMTdiM2FhOTA2ZWQwYjJiMzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYzNjcyMzg5MiwiaWF0IjoxNjM2NzIwMjkyLCJqdGkiOiJkY2JiNTVhMS0wZDY3LTQ4MDgtOGRjNy04MTdkMmE1NDA2MTUiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.ryx5xAnnMYzXIX7-U9u-W0aWumL7hSLYUzetdkJV_d5c2kIU9ww9UZE-n0nfx5Cv_GZH_pFv4bzdIi8J7x_YXbVWyQrVOKKArGqKh_MJqb4ufDBH410KPvggLIqNjhDOhs4hVgQ8HoxApEx6nkuZ3qwHAf9HjLGhNdcGfHgZT7rjYOFPFEWrmtQL1hD7dPFQsXhlWq_133c28kMel4hEz8sc7ZijI3BGhZkQW0WN05wUw2a5OVzEpc-KmKdwFiVK_mIn1XFgnk_xt_FZ0__O6GvLTgoB6lsIWTuET_N0ByWprMpA3PMvoVunWDHs8RoIGg1CEkEVOa5PtSkZX65_8g'
}

list = requests.request("GET", url2, headers=headers2, data=payload)

print(list.text)
