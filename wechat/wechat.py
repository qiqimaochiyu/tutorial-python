# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import requests
from wxpy import *
import json

robot = Bot()
def talks_robot(info='hello~'):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = 'fa8cf679361b4321a793cd6492968769'
    data = {'key':apikey,'info':info}
    req = requests.post(api_url,data=data).text
    replys = json.loads(req)['text']
    return replys

@robot.register()
def reply_my_friend(msg):
    message = '{}'.format(msg.text)
    replys = talks_robot(info=message)
    return replys

robot.start()
embed()
