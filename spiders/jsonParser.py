import json

with open('cantStudy.json') as f:
    data = json.load(f)

for i in range(len(data)):
    out = open('toDownload','a+')
    img_tag = data[i]['img']
    url = img_tag.split('=')[1].split('>')[0].split('\"')[1]
    out.write(url)
    out.write('\n')

