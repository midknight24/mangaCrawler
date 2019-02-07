import scrapy
from scrapy_splash import SplashRequest
#store urls of target websites here
import toCrawls
import time
from .. import sqlConnector
from .. import mangaList

class mangaSpider(scrapy.Spider):
    name = "manga"

    def start_requests(self):
        wait_script = """
                        function main(splash,args)
			    splash.images_enabled = false
                            assert(splash:go(args.url))
                            assert(splash:wait(1))

                            function wait_for(splash,cond)
                                local times = 0
                                while (not cond()) and (times<100) do
                                    splash:wait(0.05)
                                    times = times + 1
                                end
                            end

                            wait_for(splash,function()
                                return splash:evaljs("document.querySelector('a img') != null")
                            end)

                            return {
                                html = splash:html()
                            }
                        end
                        """
        for manga in mangaList.fetchUrls():
            name = manga[1]
            numPage = sqlConnector.getMangaPage(name)
	    urls = toCrawls.createChap(manga[0],numPage)
            page = 0
            for url in urls:
                page = page + 1
                if(page%5==0):
                    time.sleep(5)
                yield SplashRequest(url,self.parse,
                    # endpoint='render.html',
                    endpoint='execute',
                    args={'wait':3,'lua_source':wait_script},
                    meta={'name':name,'page':page}
                )

    def parse(self,response):
        #default page num
        parsedTP = 15
	chapNum = 99
        rawTotalPages = response.xpath('/html/body/table[2]/tbody/tr/td/text()').get()
	chapNum = int(rawTotalPages.split('|')[0].rsplit(" ")[1].split(u"\u8bdd")[0])
        parsedTP = int(rawTotalPages.split('|')[1].split(u'\u5171')[1].split(u'\u9875')[0])
        name = response.meta.get('name')
	sqlConnector.updateNumChap(name,chapNum)
        sqlConnector.updateMangaPage(name,parsedTP)
        yield {
            'img': response.css('a img').extract_first(),
            'totalPage': parsedTP,
	    'chapNum': chapNum,
            'name': name,
            'page': response.meta.get('page')
        }


