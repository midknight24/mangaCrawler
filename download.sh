#!/bin/bash
#read urls from toDownload and download each one using wget
count=0
while read line; do
  let "count+=1"
  declare -a arr
  arr=(${line//||/ })
  mkdir ~/manga/${arr[1]}
  wget -O ~/manga/${arr[1]}/${arr[2]}.jpg ${arr[0]} &
  if (("$count">30));then
    sleep 5
    count=0
  fi
done <$1
