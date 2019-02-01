A Scrapy crawler that crawls manga from a pre-selected website.

Splash is used to render the javascript on the page such that Scrapy can get the image url, 
which is rendered on load in the browser

A few bash scripts to automate the process. 

By default, it will crawl three times. Each time it check against MySQL database and local 
file system to see if all pages of a chapter are downloaded. Next time it will retry downloading
missing pages.
