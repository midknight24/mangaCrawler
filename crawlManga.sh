#!/bin/bash
path=~/mangaCrawler/mangaCrawler
times=3
counter=1
while [ $counter -le $times ]
do
    rm -f ${path}/rawList.json
    rm -f ${path}/jsonWatchList.json
    rm -f ${path}/toDownload
    docker restart nostalgic_gates
    sleep 3
    scrapy crawl newEpi -o ${path}/jsonWatchList.json
    scrapy crawl manga -o ${path}/rawList.json
    python jsonReader.py ${path}/rawList.json ${path}/toDownload
    bash ${path}/download.sh toDownload
    python crawlChecker.py
    counter=$[$counter+1]
done
