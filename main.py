import json

with open("data.json","r") as quiz:
    data = json.load(quiz)

print(data)