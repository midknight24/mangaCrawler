#!/bin/bash
#read urls from toDownload and download each one using wget
while read url; do
  wget -P ~/cantStudy94/ $url
done <toDownload
