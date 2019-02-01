# -*- coding: utf-8 -*-
import requests

def notifyNewChapter(name):
	requests.get("https://sc.ftqq.com/SCU43909T7887e4587fe8a3658537c33e386629275c53fcadc51d6.send?text="+name+"更新啦~")
