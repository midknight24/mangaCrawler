import scrapy
from scrapy_splash import SplashRequest
#store urls of target websites here
import toCrawls
import mangaList

class mangaSpider(scrapy.Spider):
    name = "manga"

    def start_requests(self):
        wait_script = """
                        function main(splash,args)
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
            urls = toCrawls.createChap(manga[0],20)
            name = manga[1]
            page = 0
            for url in urls:
                page = page + 1
                yield SplashRequest(url,self.parse,
                    # endpoint='render.html',
                    endpoint='execute',
                    args={'wait':3,'lua_source':wait_script},
                    meta={'name':name,'page':page}
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
	# print(response.css('a img'))
        yield {
		'img': response.css('a img').extract_first(),
	        'name': response.meta.get('name'),
		'page': response.meta.get('page')
	}


