#this mod checks against db and file sys to determine whether crawls are perfect

import sqlConnector
import os

path='/root/manga/'

names = sqlConnector.getMangaNames()

for name in names:
    numChap = sqlConnector.getNumChap(name)
    number_files = -1
    try:
        list = os.listdir(path+name[0]+'/'+str(numChap[0])) # dir is your directory path
        number_files = len(list)
    except:
        pass
    target = sqlConnector.getMangaPage(name[0])

    print("///////////////////////////////////////////////////////////////////////////////////////////////")
    print("///////////////////////////////////////////////////////////////////////////")
    print(target)
    print(number_files)
    print("////////////////////////////////////////////////////////////////////////////////////")

    if(target==number_files):
	print("---------------------------All pages download--------------------------------------")
        sqlConnector.updateCrawled(name[0],1)
#    else:
#        print("---------------------------Pages missing-----------------------------------------")
#        sqlConnector.updateCrawled(name[0],0)


