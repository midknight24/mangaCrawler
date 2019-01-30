import scrapy
from .. import watchList
from .. import sqlConnector

class spider(scrapy.Spider):
    name = "newEpi"

    def start_requests(self):
        for manga in watchList.wlist:
            yield scrapy.Request(url=manga['url'], callback=self.parse, meta={'name':manga['name'],
                                                                              'mainPage':manga['url']
                                                                            })

    def parse(self, response):

        #get result and check against db for newer epi
        result = response.css("#comiclistn dd:last-child a::attr(href)")[0].extract()
        #remove the page part
        result = result[:-5]
        result = "http://comic.kukudm.com"+result

        #number of pages in latest chp
        numPages = 15

        name = response.meta.get('name')
        url = response.meta.get('mainPage')

        #connect to db
        older = sqlConnector.getLatest(name)
        status = sqlConnector.getCrawled(name)
        if result != older or older == None or status==0 :
            #update db
            sqlConnector.update(name,url,result,numPages)
            yield {
                'url': result,
                'name': response.meta.get('name')
            }

