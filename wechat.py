# -*- coding: utf-8 -*-
import requests
import os

def notifyNewChapter(name):
	with open('notiList','a') as f:
		f.write(name+'\n')

def pushAll():
	arr = []
	with open('notiList') as f:
		line = f.readline()
		while line:
			arr.append(line.rstrip('\n'))
			line = f.readline()
	arr = list(set(arr))
	for name in arr:
		requests.get("https://sc.ftqq.com/SCU43909T7887e4587fe8a3658537c33e386629275c53fcadc51d6.send?text="+name+"更新啦~")

	os.remove('notiList')

if __name__ == '__main__':
    pushAll()
