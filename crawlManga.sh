#!/bin/bash
path=~/mangaCrawler/mangaCrawler
rm -f ${path}/rawList.json
rm -f ${path}/toDownload
scrapy crawl manga -o ${path}/rawList.json
python jsonReader.py ${path}/rawList.json ${path}/toDownload
bash ${path}/download.sh toDownload
