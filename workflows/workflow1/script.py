from google.cloud.storage import Client
import json
print('hello')

with open("data/myfile.json", "r") as f:
    data = json.loads(f.read())

print("data: ", data)
