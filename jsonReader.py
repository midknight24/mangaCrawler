import json
import sys

print(str(sys.argv))
with open((sys.argv[1])) as f:
    data = json.load(f)

for i in range(len(data)):
    out = open((sys.argv[2]),'a+')
    img_tag = data[i]['img']
    if img_tag == None:
        continue
    name = data[i]['name']
    page = data[i]['page']
    tp = data[i]['totalPage']
    url = img_tag.split('=')[1].split('>')[0].split('\"')[1]

    #append 0 in the front to avoid lexi order fuck things up
    zeros = len(str(tp)) - len(str(page))
    page_str = '0'*zeros+str(page)         

    out.write(url + "||" + name + "||" + page_str)
    out.write('\n')

