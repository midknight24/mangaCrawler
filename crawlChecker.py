#this mod checks against db and file sys to determine whether crawls are perfect

import sqlConnector
import os

path='/root/manga/'

names = sqlConnector.getMangaNames()

for name in names:
    list = os.listdir(path+name[0]) # dir is your directory path
    number_files = len(list)
    target = sqlConnector.getMangaPage(name[0])

    print("///////////////////////////////////////////////////////////////////////////////////////////////")
    print("///////////////////////////////////////////////////////////////////////////")
    print(target)
    print(number_files)
    print("////////////////////////////////////////////////////////////////////////////////////")

    if(target==number_files):
	print("---------------------------All pages download--------------------------------------")
        sqlConnector.updateCrawled(name[0],1)


