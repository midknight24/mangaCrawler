import json
import sys

print(str(sys.argv))
with open((sys.argv[1])) as f:
    data = json.load(f)

for i in range(len(data)):
    out = open((sys.argv[2]),'a+')
    img_tag = data[i]['img']
    name=data[i]['name']
    url = img_tag.split('=')[1].split('>')[0].split('\"')[1]
    out.write(url+"||"+name)
    out.write('\n')

