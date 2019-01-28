#!/bin/bash
#read urls from toDownload and download each one using wget
while read line; do
  declare -a arr
  arr=(${line//||/ })
  echo ${arr[0]}
  echo ${arr[1]}
  wget -P ~/manga/${arr[1]}/ ${arr[0]}
done <$1
