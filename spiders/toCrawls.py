# 'http://comic.kukudm.com/comiclist/2274/68949/'

def createChap(url,num):
    urls=[]
    for i in range(num):
        urls.append(url+'%s.htm' % i)
    return urls