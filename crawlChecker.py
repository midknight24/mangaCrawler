#this mod checks against db and file sys to determine whether crawls are perfect

import sqlConnector
import os

path='/root/manga/'

names = sqlConnector.getMangaNames()

for name in names:
    list = os.listdir(path+name) # dir is your directory path
    number_files = len(list)
    target = sqlConnector.getMangaPage(name)
    if(target==number_files):
        sqlConnector.updateCrawled(name,1)


