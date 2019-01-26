import scrapy
from scrapy_splash import SplashRequest
#store urls of target websites here
import toCrawls
import mangaList

class mangaSpider(scrapy.Spider):
    name = "manga"

    def start_requests(self):
        #urls = ["http://comic.kukudm.com/comiclist/2035/68893/2.htm",]
        for manga in mangaList.mangaUrls:
            urls = toCrawls.createChap(manga,20)
            for url in urls:
                yield SplashRequest(url,self.parse,
                    endpoint='render.html',
                    args={'wait':3},
                )

    def parse(self,response):
        # part = response.url.split("/")[-1]
        # page = part.split(".")[-2]
        # filename = 'manga-%s.html' % page
        # with open(filename, 'wb' ) as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
	#print("hi there////////////////////////////")
	#print(response.body)
	print(response.css('a img'))
        yield {
		'img': response.css('a img').extract_first()
	}
