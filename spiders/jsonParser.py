import json

with open('cantStudy.json') as f:
    data = json.load(f)

print(data[1]['img'])
