# wlist=[
#     {'url':'http://comic.kukudm.com/comiclist/2274/index.htm',
#     'name':'cantStudy'}
#     ]

import json

json_path = './jsonWatchList.json'

def fetchUrls():
    with open(json_path) as f:
        data = json.load(f)
    mangaUrls = []
    for i in range(len(data)):
        sublist = [data[i]['url'],data[i]['name']]
        mangaUrls.append(sublist)
    return mangaUrls


#mangaUrls = [['http://comic.kukudm.com/comiclist/2359/68967/','tester'],]
